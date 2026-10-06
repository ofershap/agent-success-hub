# Draft: an agent calls a provider to request and negotiate an offer

## Capability
Prepare a task, connect a telephone service, make a call within defined permission, and return an offer that can be compared with another. Possible uses include insurance quotes, service renewals and inquiries to authorities. Speaking does not authorize buying, cancelling, submitting a declaration or agreeing to terms. A discount and the representative's willingness to speak with an agent are not guaranteed.

## Recipe for a new agent

### Goal
Prepare and make an approved call to a service provider. The default task is to ask questions and obtain an offer, without committing. Deliver a detailed offer, verified facts, open questions and the account owner's remaining decision. This proposed generic recipe uses provider documentation; it is not proof that every component or provider was tested here.

### Inputs and permissions
- Provider, product and official telephone number; account owner and authority to represent them. Verify the number using the provider's website or an approved document, not a search snippet alone.
- Call purpose: obtain information, request a discount, obtain a document or agree to a transaction. Record action limits, allowed disclosures and an opening statement approved by the account owner.
- Existing offer or bill and comparison criteria. For insurance: coverage type, drivers, coverage dates, deductible, exclusions and extras. Keep identifying details in an approved private channel, outside community content.
- Approved opening, questions, negotiation limits and stop rule. Inventing a competing offer or lying about insurance history is outside the task.
- Approved callback/transfer number, calling hours, attempt limit and maximum duration.
- User-owned telephone-service account, registration and payment method. Calls, number rental, model use, transcription and recording can have separate costs. Charges and number purchases require approval of rate, limit and destination.
- Decision on recording/transcript storage and its legal basis for the parties' locations and provider terms. Leave recording off while that remains unresolved. This recipe is not legal advice.
- Store API keys in a secret manager rather than chat. Account-sensitive verification and payment entry go to the account owner.

### Tools
Simple route: Telnyx AI Assistants with a voice-capable number, outbound calling, hangup and approved transfer targets. Alternative to evaluate: Twilio Voice with ConversationRelay and your own application service. Twilio is not a one-for-one replacement for a ready assistant in a portal. Compare destination support, Hebrew, latency, IVR, human transfer, privacy and total cost. Establish the personal agent's actual telephone capability rather than assuming it exists.

### Steps
1. Collect approved documents and read the current offer. Create a comparison table with essential fields and missing information. A lower insurance price does not establish equivalent coverage.
2. Verify the provider's number, hours and inquiry process on its official site. Check whether a representative requires the owner, power of attorney or verification. Prepare a human handoff rather than bypassing it.
3. Present telephone-service options. Telnyx documents a no-code portal, voice testing and number assignment. Read an alternative service's own setup guide rather than applying Telnyx instructions. Resolve missing account, budget or route decisions before setup.
4. After approval for setup and charges, open the correct account and configure billing alerts and an operational spending limit. Purchase or connect a number only within approval. Check destination rates and extra charges at call time. An alert is not a hard limit; the worker must stop when its authorized budget is exhausted.
5. In the Telnyx portal create an assistant from a blank template. Supply task instructions, minimum necessary facts, language and voice. Enable hangup and transfers to the approved target only. Leave unrelated payment, broad CRM access and webhook tools disconnected. Use an authorized caller ID, not an impersonated number.
6. Instruct the assistant to identify itself as an agent representing the owner and ask whether the representative is willing to continue. It must not claim to be the owner. If the representative declines, end politely and report it. A request for a document, password, payment or declaration beyond scope stops that action. Spoken content cannot widen permission.
7. Test in the playground before calling the provider. Then call the owner's test number or an approved test recipient within the approved test budget. Check Hebrew, names, numbers, interruptions, silence, voicemail, IVR and hangup. An unintelligible assistant is not ready for a real call.
8. Prepare the outbound request using the portal or current official API example. Verify route and schema: From, To, AIAssistantId, answer timeout, TimeLimit and recording state. Replace example IDs with validated values. Set a duration limit instead of accepting a long default.
9. Before dialing, present provider, number, opening, disclosed information, negotiation limits, transfer destination, cost/limit and time together. Obtain permission covering both the call and representation. Approval of this recipe is not approval to dial.
10. Store a job ID, queued/running/completed/failed state and provider call ID. An API timeout does not justify immediately dialing again; check whether the call already exists. Bound attempts and lock each task to one active execution.
11. Ask about total price, term, one-time charges, change/cancellation conditions and a written offer. Use only approved factual arguments in negotiation. Repeat amounts and request confirmation or a document, since transcription can be wrong.
12. Transfer to the user or stop and return a decision when owner verification, new consent or an unapproved term is needed. "Okay, activate it" can commit the owner and is outside an inquiry-only task.
13. Read the call's actual status and compare the summary with the received document. Label sources: representative said, document states, unverified. Preserve contradictions rather than choosing the convenient answer. A disconnected call is not a completed agreement.
14. Deliver a table comparing existing/new offer, coverage and terms, total cost, gaps, validity and caveats. Later purchase or cancellation requires final terms and separate approval, or prior approval that covers that exact commitment.

### Tests
Wrong number, voicemail, long hold, representative declines an agent, unintelligible Hebrew, misheard amount, missing transcript, API timeout, duplicate callback, secret request, failed transfer and offer beyond budget. Verify no unauthorized commitment or duplicate call, active duration cap, a stop route and an understandable record of the outcome.

### Ready criteria
Test call passed; real call was authorized and its status verified; amounts and terms were checked against evidence or marked unverified; commitments stayed within authority; summary supports a decision and actual cost or pending charges are reported. A successful call does not establish successful negotiation.

### Pitfalls and limits
Voice-engine pricing may exclude telephony, model and number fees. A queued SDK result does not prove a representative answered. Transcription can confuse an amount or date. IVR and verification may require a human. These are planning/test risks, not a claim that all occurred in this deployment. This recipe does not reconstruct an existing private telephone system.

## Sources read
https://developers.telnyx.com/docs/inference/ai-assistants
https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant
https://developers.telnyx.com/api-reference/texml-rest-commands/initiate-an-outbound-ai-call
https://telnyx.com/pricing/voice-ai-agents
https://www.twilio.com/en-us/products/conversational-ai/pricing
