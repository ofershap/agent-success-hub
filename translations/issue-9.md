# Draft: an agent-assisted growth loop for an open-source project

## Capability
Assess a project as a new user, fix adoption barriers, prepare relevant distribution and measure the result. This excludes buying stars, spam and traffic promises. It contains no story about a particular person or unverified success numbers.

## Recipe for a new agent

### Goal
Build a measured growth loop for an open-source project: baseline -> first-use test -> fixes -> approved distribution -> measurement -> next experiment. The first goal is for the right person to understand and use the project, rather than maximize the number of posts.

### Inputs and permissions
User-owned repository URL, version/commit, license, target audience, problem solved and alternatives. Obtain runtime, build instructions, demo if available and permission to read traffic/download data. Specify who may merge, release and publish on each channel. Collect factual text and sources for each claim. Without analytics, a traffic baseline is unavailable; start with local test metrics only. Set an experiment window, permitted channels, budget and time limit. Outreach drafts do not authorize sending.

### Tools
Git/GitHub, a sandbox without secrets for code testing, runtime matching the lockfile, a browser for docs/demo tests, issue tracker and private metrics spreadsheet/file. Use GitHub/registry data that the account may access; keep private traffic data unpublished. Buying marketing tools is unnecessary.

### Steps
1. Read the README, license, release notes, issues and PRs. State in one sentence who the project is for, what it does and what it does not do. Leave unsupported claims out of promotion.
2. Freeze a baseline with date, commit and version. Record only sourced metrics: views/unique visitors, clones, downloads, stars, issues and demo results. Record the time range and each metric's definition; these are not all "users". Mark absent data unavailable rather than zero.
3. Run a first-use test in a clean, isolated environment. Read scripts before installation. Follow the README exactly: installation, import/API, minimal example and build. Use only files and knowledge a new reader will receive. Record missing steps, time to result, errors and environment.
4. Test the demo as an external user: fresh session, mobile/desktop, console errors, instructions and failure states. For a sync project, for example, test two contexts and disconnection/reconnection according to its documented contract. Do not invent capabilities the code does not claim.
5. Prioritize broken installation/docs/demo ahead of new features. Create a small reproduction for each barrier with expected and actual behavior. Show the owner the text and destination before opening a public issue. Search for an existing issue to avoid duplicates.
6. Prepare README, quickstart and example fixes in a separate PR. Each example must run on the version being distributed. Verify commands in a clean environment, links and license. For new code, run regression tests, build and diff review. Merging and releases require permission.
7. Prepare an asset pack: factual opening, problem, suitable use, tested snippet, demo image inspected visually, limitations and canonical link. User details, conversations and analytics require permission before use as public evidence.
8. Select channels for audience fit: a technical discussion, forum, dev.to/blog or community already discussing the problem. Read each destination's current rules and self-promotion policy. Reddit and individual subreddits do not automatically permit promotion. If unclear, prepare a draft or moderator inquiry for review.
9. Write a short channel-specific message explaining what helps the reader, disclose that you are the creator or acting for the project, and include limits and an example. Do not pose as an outside user recommending it. Avoid copying one post into dozens of communities or requesting fake engagement.
10. Present community/channel, account, text, media and timing together to the owner. After approval, check that it has not already been sent or answered and the channel rules are unchanged. Send once and save the actual URL. Stop when a moderator requests removal or a channel restricts automation.
11. If replies are permitted, answer relevant comments within that permission. Return undocumented questions to the owner instead of promising features. Criticism and bugs are product data rather than targets for manipulating metrics.
12. At the experiment window's end, read the same measurement sources using the same definitions. Separate referrals, downloads and conversions where valid measurement exists. A change alongside a post is not proof of causation; releases, bots or other channels may affect it. Star count alone is insufficient.
13. Report actions, URLs, baseline/end metrics, fixed adoption barriers, feedback, cost and caveats. Select one next experiment from feedback rather than "more posts". Future monitoring needs a scope and end date; this recipe does not create permanent outreach.

### Tests
README works from a clean environment; example matches version; demo pixels inspected; links valid; marketing matches facts; code/issues/metrics disclose no secret; no duplicate issue/post; channel permits the post; analytics sources and ranges match. Without telemetry, make no growth claim.

### Ready criteria
A new user can reach a working example using the instructions alone, or blockers are defined. Distribution materials are checked and ready for review. If publication was approved, its link is verified. The experiment report shows data actually read and separates product fixes, promotion and business outcome. Drafts and unperformed publication are labeled accordingly.

### Pitfalls and limits
Stars are not users; clones/downloads may include CI/bots; different analytics windows do not provide a comparison. Post engagement is not product adoption. Community code is not the agent's own code. A channel may forbid self-promotion despite past similar posts. These are recipe limits, not outcome data.

## Public sources read
https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-code-of-conduct-to-your-project
https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-a-summary-of-repository-activity
https://www.redditinc.com/policies/content-policy

Read the specific destination's rules and project data when applying the recipe. These sources do not authorize posting in a particular community.
