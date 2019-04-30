Reading https://geoff.greer.fm/2017/02/28/software-rot/ gave me some thoughts.

There will be a point that a code base become too big, too much code, to much debt, that changing software architecture would be hugely expensive. The article shows me the story about Firefox trying to catch up Chrome's multi-process, but couldn't since Chrome is designed with multi-process in mind from ground up.

Over time, any software project accumulates **scars** into its code base. Scars are fixes for edge cases. Scars are an competitive advantage of a veteran software, since it covers all the edge cases which are important to users. But that's a double edge knife. We can't just simply build vNext from ground up since that means giving up scars and breaks existing user experience.

This enables an opportunity for new startup. The context will change, and there will be some requirements that the Big Old Software couldn't not handle easily. New start up could start working from a new MVP which carefully designs with what worked/didn't work with Big Old Software, as well as emerging requirements in mind. They could start with a niche, charge a smaller amount of money, then gradually build up.

Therefor, there will be opportunity for reinventing old things. Startup needs to understand Big Old Software well, and keep track of surrounding environment changes to detect the opportunity.

Let's make an example. Slack is dominating productive chat market. They built their app with Electron, which is resource heavy, but let them to iterate faster and make the software highly extensiable. But what if there's a point that the app too slow, and the hardware isn't fast enough anymore. In that case, fast and lightweight is the new requirements that they can't easily achieve. New startups can start from building fast, native version of Slack, which could be a niche, and gradually expand the market.

So it's not about there isn't enough opportunity. It's about whether or not you have sufficient skills to grab new opportunity quickly.
