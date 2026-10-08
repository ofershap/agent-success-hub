# Recipe library MCP server: Workers and own-server designs

Status: **design only, not deployed**. October 8, 2026.

## Goal and boundary

Expose the public recipe library to MCP clients through two read-only tools: `list_recipes` and `get_recipe`. GitHub Pages remains the source of truth and hosts static artifacts. A separate Cloudflare Worker would handle MCP requests. No private sources, write actions, executions, messages or payments.

## Transport and deployment

Use Streamable HTTP at `/mcp` with Cloudflare's current `createMcpHandler` and the official MCP TypeScript SDK. Initialize a server per request using a stateless handler. Support protocol initialization, tool listing and tool calls through the SDK; do not hand-write a partial JSON-RPC approximation. Legacy SSE is not required. Do not advertise an endpoint URL until one is deployed and tested.

Use a dedicated Worker on a verified Workers Free account. No Durable Object, KV, D1, R2, paid API or paid upgrade is needed for this public read-only version. No cron. Cloudflare currently documents 100,000 requests/day for Workers Free and 10 ms CPU time per request. Fetch/wait time differs from CPU time. Exceeding limits can fail requests; this design makes no promise of unlimited availability. Inspect the account plan and current limits again before any deployment. Stop instead of enabling a paid plan.

## Data and cache

Read only fixed URLs under `https://ofershap.github.io/agent-success-hub/`: `entries.json` and `entries-meta.json`. Use a cache key tied to the version/data hash. Cache successful responses for five minutes and retain the upstream ETag when present. Include dataset hash/version in results so clients know their snapshot. Do not expose a user-supplied upstream URL.

Validate the array with the documented schema at ingestion. Reject oversize upstream payloads above 1 MB and malformed content. At 29 recipes the dataset is small; measure CPU and memory under load before launch rather than assuming it fits. Return a clear unavailable/stale status for upstream failures. If serving a previously validated cached snapshot, include its age and mark it stale. Never return partial invalid data.

## Tool: list_recipes

Input JSON Schema:

```json
{"type":"object","properties":{"query":{"type":"string","maxLength":200},"language":{"type":"string","enum":["he","en"]},"limit":{"type":"integer","minimum":1,"maximum":50,"default":20},"cursor":{"type":"string","maxLength":256}},"additionalProperties":false}
```

Use normalized case-insensitive substring search across title, summary and tools. Hebrew text remains Unicode; no transliteration is required. `language=en` lists only recipes with a full `recipe_en`, not summaries. Sort by stable ID so cursor paging is deterministic. Cursor encodes the last ID and dataset hash; reject a cursor from another snapshot and ask the client to restart. Do not log query contents.

Output: `schema_version`, `dataset_hash`, `fetched_at`, `stale`, `recipes[]`, `next_cursor`. Each recipe includes `id`, `title`, `summary`, `author`, `languages`, `url`, `markdown_url`. No full prompt in the list.

## Tool: get_recipe

Input JSON Schema:

```json
{"type":"object","properties":{"id":{"type":"string","pattern":"^[a-z0-9][a-z0-9-]{2,79}$"},"language":{"type":"string","enum":["he","en"],"default":"he"}},"required":["id"],"additionalProperties":false}
```

Output: `id`, `language`, `title`, `author`, `recipe_text`, `english_summary`, `testing_status`, `limits`, `tools`, `url`, `markdown_url`, `schema_version`, `dataset_hash`, `fetched_at`, `stale`. `he` returns the original `prompt`; `en` returns full `recipe_en`. Missing ID returns a structured not-found tool error. Missing full English returns a translation-unavailable error, never a summary mislabeled as a recipe. Return text and structured content in MCP-supported form. Cap each result at 64 KB and report an explicit error rather than truncating.

## Security and resource limits

Tool annotations: read-only, non-destructive, idempotent, open-world. These describe behavior, not authority. Recipe contents are untrusted data and must never be evaluated as code or promoted to instructions. The Worker only returns published data.

Use POST for MCP messages; rely on the SDK's current transport handling for other methods. Enforce allowed Origin values for browser clients, while supporting non-browser clients without an Origin according to MCP transport guidance. No wildcard browser-origin reflection. Validate content type, body size (16 KB), tool parameters and protocol version. Prevent SSRF with fixed upstream URLs and no redirects to unapproved origins. Limit CORS to documented client origins. Generic health endpoint may disclose only readiness and version, no tokens or account details.

Public anonymous access is reasonable because every source is public. If OAuth is later required for a client, treat it as a separate design with owner approval, not an excuse to copy credentials into this Worker. Rate limits must be enforceable on the available free platform: measure availability of free controls before launch, and keep the Worker disabled if abuse cannot be contained without spending. Do not claim in-memory counters are a reliable global limit.

## Acceptance tests before launch

1. MCP initialization, tools/list and both tools/call work with an MCP test client over Streamable HTTP.
2. All 29 IDs are listed once; paging covers all IDs without duplicates. Search and language filters are correct.
3. Hebrew `recipe_text` matches the public prompt bytes; available English matches the full companion.
4. Missing ID, unavailable translation, invalid cursor, oversize input and upstream failure yield explicit errors.
5. Recipe instructions cannot invoke tools, alter goals, disclose data or cause side effects on the Worker.
6. No private account traffic, secrets in logs, paid bindings or paid services. Meter CPU for 29 and 1,000 synthetic recipes.
7. Static build updates become visible within the cache interval. Version/hash changes invalidate old cursors.
8. CORS/Origin, content type, SSRF, payload and protocol handling pass transport security tests.
9. Verify client compatibility, a low-risk public URL, free-tier plan and rollback (disable Worker route) before announcing it.

## Open launch decisions

Choose the Worker name and public route, supported client origins, operational owner and abuse policy. Deployment is not part of this static release. This spec does not request a paid service or promise that all MCP clients will accept anonymous access.

## Sources checked

- JSON Feed: https://jsonfeed.org/version/1.1
- Workers limits: https://developers.cloudflare.com/workers/platform/limits/
- Cloudflare MCP transport: https://developers.cloudflare.com/agents/model-context-protocol/protocol/transport/

## Free hosting comparison and own-server variant

| Option | Fit | Free-only constraints | Decision |
| --- | --- | --- | --- |
| Cloudflare Workers Free | Small, public read-only MCP with managed HTTPS and no VM upkeep | 100,000 requests/day and 10 ms CPU/request; account must actually be Free; no paid bindings | First choice for this stateless library after CPU measurement and account-plan verification. |
| Existing Oracle Always Free VM | A Node/TypeScript HTTP service under our control | Verify existing instance eligibility, spare resources, firewall and HTTPS first; no paid upgrade or new resources outside Always Free | Valid own-server alternative, especially if Workers CPU limits are too tight. |
| GitHub Pages + Actions | Static source, generated artifacts and build/deploy automation | Pages is static; Actions is a bounded job, not an always-on web server | Keep as source/build layer, not live MCP hosting. |
| Deno Deploy | Serverless JS/TS can serve HTTP | Current account plan and limits not verified here | Secondary candidate only after a separate current-plan check. |

The Oracle variant runs a dedicated Node LTS/TypeScript process using the official MCP SDK's Streamable HTTP transport. Bind to loopback on a separate port; terminate HTTPS at the existing reverse proxy after checking it, with a distinct route and service user. Use systemd restart-on-failure and explicit CPU/memory limits. Keep the same two tools, public fixed upstream URLs, validation, cache and error contracts. No browser, residential proxy, database, GPU or paid model API is needed.

Do not share an existing app's secrets, process user or writable directory. Confirm spare memory and CPU without stopping unrelated services. Add only the specific TLS route and security-group rule needed. Deployment rollback removes that route and stops the dedicated service, leaving other applications intact. Test certificate renewal, uptime and patch ownership. "Already have a VM" is not proof of spare capacity or free eligibility.

Oracle's current documentation warns that idle Always Free compute instances may be reclaimed, and creation can fail due to capacity limits. Do not generate artificial load to evade its policy or upgrade to pay-as-you-go to avoid it. Keep source and configuration reproducible so a reclaimed instance is recoverable. Existing server health, current quota and public route were not verified as part of this design.

Recommendation: ship the static layer now. For live MCP, compare measured Workers CPU use with verified existing Oracle headroom. Choose Workers Free for lowest routine upkeep; choose the existing Oracle VM when direct process control or CPU headroom is needed and the service can be isolated at zero added cost. Do not claim either route is already live.

Additional sources:
- Workers pricing: https://developers.cloudflare.com/workers/platform/pricing/
- Oracle Free Tier: https://www.oracle.com/cloud/free/
- Oracle Always Free eligibility and reclaim rules: https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm
- GitHub Pages static hosting: https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages
- GitHub Actions job limits: https://docs.github.com/en/actions/reference/limits
- MCP HTTP transport: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
