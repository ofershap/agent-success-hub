# Draft: designing and building a website with an agent, from brief to live verification

## Capability
Turn a goal and content into a design system and usable responsive website. This is a shareable workflow rather than a copy of a personal website or a service's internal instructions. The result includes design decisions, code, tests and handoff, rather than only an attractive screenshot.

## Recipe for a new agent

### Goal
Design and build a website for a defined purpose with approved content and a clear primary action. Keep a preview for review until publication is approved. On an existing site preserve URLs, content, functionality and identity unless asked to change them. This proposed recipe does not claim a fresh end-to-end test on an independent project.

### Inputs and permissions
- Audience, what they need to know/do and what counts as success. The owner chooses the business goal.
- Website type, pages, languages/RTL, approved content, brand assets, licensed images and links.
- Two to four references and what the owner likes about them. Learn hierarchy/spacing rather than copying a brand or its assets.
- Repository, stack/runtime/lockfile, hosting/domain and owner account. For a new site choose a minimal stack and explain tradeoffs before a major decision.
- Functional requirements: forms, API, search, analytics and authentication. Each has privacy and cost implications. A form must not look operational while disconnected.
- Separate access, editing and publication permissions; preview/branch and approver. Missing content remains a blocker or labeled preview placeholder, rather than an invented production fact.

### Tools
Code editor, Git, project runtime, dev server, build/tests and browser for viewport screenshots and link/accessibility checks. HTML/CSS/JavaScript suffice for a simple website; retain the existing framework without a reason to replace it. Paid assets and services require approval.

### Steps
1. Read the website and repository: pages, routes, components, style tokens, build/deploy and tests. Check Git and concurrent changes. Save baseline screenshots and URLs.
2. Write a short brief: audience, primary action, mandatory content, limits and style. Gather missing content. Keep invented testimonials, client names and success numbers out.
3. Open references and inspect pixels. Analyze headings/text, grid, content width, contrast, images and spacing. Record what to adopt and what to leave out. Another site's screenshot is not your own design.
4. Build information architecture: pages/sections, primary action and navigation. Let the brief set the order rather than a fixed template. Sketch a narrow-screen wireframe before choosing colors.
5. Define design tokens: background/surface/text/action, language-supporting font, typography, spacing, radius and maximum width. Check contrast and maintain consistent values.
6. Build one direction as a preview with real content and complete structure. Make the site's identity, audience and action clear. Show significant brand decisions to the owner before full implementation.
7. Write semantic HTML: header/nav/main/footer, hierarchical headings, buttons for actions, links for navigation, form labels and useful alt text. Avoid clickable divs inaccessible to keyboards.
8. Build mobile-first using grid/flex and flexible units. Place breakpoints where content breaks. For RTL use logical properties and suitable direction for code/URLs. Test long text and mixed languages.
9. Use approved assets only. Set image dimensions to prevent layout shifts, suitable sizes and loading behavior. Keep text as text. Core content must remain available without animation.
10. Connect only scoped features. Forms need validation, success/error states, approved data destination, privacy/consent and risk-appropriate spam protection. Client code must contain no API secrets. Search needs loading/empty/error states. Authentication/payment require separate design and permission rather than a mock appearing functional.
11. Run build/lint/tests. Check routes, links, 404, content-based title/meta/canonical, and absence of private information in assets/source maps. Keep previews private/unindexed unless public access is intended and approved.
12. Open in a browser and inspect pixels: narrow (~390px), medium and wide (~1440px) viewports, 200% zoom, long content and fully loaded assets. Check overflow, crop, footer, sticky elements, menu, RTL and form states. Save screenshots of key screens/states, fix issues and check again.
13. Test keyboard-only use: tab order, visible focus, enter/space, escape for dialogs; reduced motion and basic accessibility. Automated checks complement rather than replace manual tests.
14. Deliver a preview with diff, decisions and known gaps. Before publication recheck account/domain/branch. Get approval for final content and audience. Design approval does not authorize domain purchases or DNS changes that disable a website.
15. Publish to approved hosting, read the deployment result and open its returned URL. Verify page, assets, routes, actions and screen sizes. HTTP 200 is insufficient. A failed deploy leaves the prior live version; avoid quietly bypassing checks.
16. Deliver live URL, commit, reproduction commands, tokens/components, gaps and rollback. Document where to edit content and how to test it. A redesign alone does not support SEO/conversion promises.

### Tests
Displayed content matches approval; build; routes/links; secrets; mobile/desktop pixels; RTL; loaded images; form success/error; keyboard/focus; zoom/contrast; loading/empty states; console/network errors; production readback. Test forms only with authorized test data and recipients.

### Ready criteria
No unapproved placeholder; clear action; no unintended cropping or overflow; functions work or are labeled unfinished; pixels inspected at relevant sizes; owner review/publication within authority; live URL verified and rollback available. A ready preview is not a published website.

### Pitfalls and limits
A build is not a visually checked design. Screenshots before image loading mislead. RTL numbers/code need testing. Global CSS can break another component. Mock forms are not operational forms. One screenshot cannot test every screen or accessibility. These are implementation risks rather than business outcome claims.

## Sources read
https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
https://www.w3.org/WAI/tutorials/page-structure/
