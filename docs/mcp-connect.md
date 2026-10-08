# Connect an agent to the recipe library

Endpoint: https://recipes.gitshow.dev/mcp
Transport: Streamable HTTP. Authentication: none. Read-only public content.

In an MCP-compatible agent, add a remote server, paste the endpoint and choose Streamable HTTP. A host may call this a custom connector, remote MCP server or app. Client-plan support varies; use your host's current connection settings.

Example configuration for clients accepting URL-based MCP servers:

```json
{"mcpServers":{"recipe-library":{"url":"https://recipes.gitshow.dev/mcp"}}}
```

Use `list_recipes` to search by query, page with its cursor or filter for full English recipes. Use `get_recipe` with a returned ID and language `he` or `en`. Example: `get_recipe({"id":"issue-25","language":"he"})`.

The library currently has 29 recipes and six full English companions. Other English fields are summaries, not complete translations. Missing IDs and missing full translations return explicit errors. Fetching a recipe gives no permission to send, spend or access accounts. Review the recipe and authorize your own agent separately.

The server reads the published GitHub Pages dataset. Refresh is normally within five minutes; upstream failures can return a last validated snapshot up to one hour old, explicitly marked stale. Free hosting has no uptime guarantee. `GET /mcp` is not a webpage or a connection test; use MCP initialization. Readiness: https://recipes.gitshow.dev/health

Static fallbacks: [API contract](api.md), [JSON Feed](feed.json), [full corpus](llms-full.txt), [schema](entries.schema.json). Submit recipes through https://ofershap.github.io/agent-success-hub/submit.html .
