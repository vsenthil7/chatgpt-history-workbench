You are acting as a skeptical market analyst, not a builder. 
Do not write any code, architecture, or product spec in this session. 
If you are tempted to design the product, stop and return to evidence.

CONTEXT
I am a solo technical founder. I can build almost anything alone and fast.
I will NOT do customer interviews, sales calls, cold outreach, or networking.
I have no ad budget. My only viable channels are written content, SEO,
marketplace listings, and public communities.
I have built 40+ projects over 6 years and earned zero revenue from them.
The failure has never been building. It has always been reaching a buyer.

PROBLEM STATEMENT TO INVESTIGATE
A growing number of capable people are disengaging from socialising.
They can build products but will not (or cannot) do the human-facing work
that selling normally requires. I want to know whether this group is a real,
reachable, paying market — and if so, what product serves them.

DELIVER THESE SEVEN SECTIONS, IN ORDER. Use web search throughout and
cite every factual claim with a source link.

1. IS THE TREND REAL?
   Find hard data on declining socialising, rising solo/indie entrepreneurship,
   and founders who report marketing as their blocking constraint. Give numbers.
   If the evidence is weak, say so plainly.
2. WHO EXACTLY IS THE BUYER?
   Define 2-3 specific segments. For each: their job, what they have already
   built, what they currently spend money on, and where they post publicly.
   Reject vague segments like "indie hackers".
3. THE MARKET SIZE, HONESTLY
   Estimate how many people are in the best segment and what share would pay.
   Show your arithmetic. State your confidence and what would change the number.
4. WHAT ALREADY EXISTS
   Find 8-12 existing products aimed at this pain. For each: what it does,
   price, and — most importantly — what users complain about, quoted from
   public reviews, Reddit threads, or forum posts. This is the gap analysis.
5. THE CENTRAL TRAP
   A product for people who won't market themselves must still be marketed
   to them. Address this directly. Find real examples of products that solved
   it and explain the mechanism they used. If you cannot find any, say so.
6. THE COLD-START PLAN
   Describe exactly how the FIRST 10 paying customers arrive, using only
   written content, SEO, marketplaces, or public communities. No calls,
   no ads. Name specific keywords, specific subreddits or forums, specific
   search volumes. If no credible route exists, say that instead of inventing one.
7. VERDICT
   Give one of three answers: BUILD, DON'T BUILD, or NEEDS MORE EVIDENCE.
   Then list the three specific facts that would flip your verdict.
   Then list explicit kill criteria: what result at 30, 60 and 90 days
   would mean abandoning this.

RULES
\- Every claim gets a source. No unsourced assertions.
\- Where evidence is thin, say "weak evidence" rather than filling the gap.
\- Do not be encouraging. Assume I will build whatever you validate,
  so validate carefully.
\- Do not propose features. Section 7 ends the session. you ahve full permisison to search in web dont wait for me

Read 16 pages, searched the web, updated tasks

## Market Analysis: "Capable builders who won't sell"

**Two research failures up front, because they change how much weight you should give some sections.** Reddit is entirely unreachable from this environment — reddit.com, old.reddit.com, mirrors and Wayback snapshots are all blocked. I have no Reddit quotes and no verbatim subreddit rules. And I could not obtain a single real monthly search volume: every free keyword tool is JavaScript-rendered, robots-blocked or egress-blocked. Section 6 is weaker than it should be because of this, and I've flagged where.

---

### 1. IS THE TREND REAL?

**Verdict: two of the three sub-claims are real. The link between them — which is the whole thesis — has no evidence at all.**

**(a) Declining socialising — STRONG evidence.**

US Bureau of Labor Statistics, American Time Use Survey: time spent socialising and communicating fell to **35 minutes per day in 2025, from 41 minutes in 2015**; participation on a given day fell from **38% to 30%** ([BLS ATUS 2025](https://www.bls.gov/news.release/atus.nr0.htm)). Over 20 years it is **45 → 35 minutes, a 22% fall**, with 15–24s dropping from roughly an hour to 35 minutes ([Axios, 5 Jul 2026](https://www.axios.com/2026/07/05/americans-socializing-decline)).

Survey Center on American Life: men reporting **no close friends rose from 3% in 1990 to 15%**; men with six or more close friends fell from **55% to 27%** ([SCAL](https://www.americansurveycenter.org/commentary/american-men-suffer-a-friendship-recession/)).

**(b) Rising solo entrepreneurship — MODERATE evidence.**

Census: **29.8 million nonemployer businesses** in 2022, generating **$1.7 trillion, 6.8% of the US economy** ([Census](https://www.census.gov/library/stories/2025/05/smallest-businesses.html)). Business applications are running at **531,728 in August 2026** — but that figure is **down 7.8% month-on-month**, so the formation trend is flat-to-falling right now, not accelerating ([Census BFS, Aug 2026](https://www.census.gov/econ/bfs/pdf/bfs_current.pdf)).

Within software specifically: **45.7% of Freemius SaaS makers are solo-founded**, and roughly **50% of MicroConf's \~700 surveyed independent SaaS products** are solo ([Freemius, State of Micro-SaaS 2025](https://freemius.com/blog/state-of-micro-saas-2025/)).

**(c) Marketing as the blocking constraint — MODERATE on hard numbers, strong qualitatively.**

From the same Freemius report: **\~70% of micro-SaaS earn under $1,000 MRR**; **57% of founders running paid ads either wait 7+ months for ROI or cannot tell whether the ads work**; **47%** now find integrations, partnerships and communities more dependable than paid acquisition; **50%** rely on communities and referrals as their primary channel.

Ahrefs' own database statistics explain why the content route is so slow: **96.55% of pages get zero Google search traffic**, **1.74% of new pages reach the top 10 for any keyword within a year**, and **72.9% of current top-10 pages are over three years old** ([Ahrefs SEO statistics](https://ahrefs.com/blog/seo-statistics/)).

**(d) The link between (a) and (b) — NO EVIDENCE.**

This is the finding that matters. I searched for it and found nothing. There is no survey, no dataset, and no study showing that founders who socialise less are more likely to be blocked on distribution, or that the declining-socialising population overlaps with the building population. The ATUS decline is a general-population trend driven substantially by screens and streaming — **television alone is 2.6 of the 5.2 daily leisure hours** ([BLS](https://www.bls.gov/news.release/atus.nr0.htm)). It is not evidence of a new class of capable-but-withdrawn builders.

You have fused two real, independent trends into one imagined segment. That fusion is the weakest load-bearing beam in the whole thesis, and everything downstream inherits the weakness.

---

### 2. WHO EXACTLY IS THE BUYER?

I am defining segments by **observable behaviour plus existing spend**, because that's the only way to reject "indie hackers."

#### Segment A — Marketplace app developers ranked outside the top tier (STRONGEST)

**Who:** Someone with a live, published listing on a platform marketplace, usually a working developer or freelancer, whose app sits below the fold in its category.

**What they've already built:** A shipped, reviewed, installable product. This is the qualifying behaviour — they cleared a platform review process.

**What they already spend:** Platform revenue share (Shopify: 0% on the first $1M lifetime from Jan 2025, then 15%, plus 2.9% processing — [Shopify dev docs](https://shopify.dev/docs/apps/launch/distribution/revenue-share)). Ranking tools at **$29–$99/month** ([App Store Analytics](https://www.appstoreanalytics.io/)). Directory submission at **$499–$999 one-time** ([ListingBott](https://listingbott.com/)). Content generation at **$99–$999/month** ([Byword](https://byword.ai/pricing/)).

**Where they post publicly:** Shopify Partners community forum, Atlassian Developer Community, Chrome extension developer groups, and the app-review sections of the marketplaces themselves.

**Why this segment is the best one:** their distribution surface is a search box with rules, not a human. **60% of Shopify App Store installs come from search** — Shopify's own figure ([Shopify Partners blog](https://www.shopify.com/partners/blog/app-store-ads)). That is the only channel in this entire report where a non-social founder can compete on merit.

#### Segment B — Bootstrapped micro-SaaS operators at $1K–$5K MRR

**Who:** Founders past validation but stuck. **18% of micro-SaaS sit in the $1K–$5K MRR band**, median profitable micro-SaaS \~$4.2K MRR ([Freemius](https://freemius.com/blog/state-of-micro-saas-2025/)).

**What they already spend:** The full incumbent stack in Section 4 — $39–$499/month on Reddit monitoring, $25–$2,000/month on SEO content, $900 on done-for-you Product Hunt launches ([Tetriz](https://www.tetriz.io/product-hunt-launch/)).

**Where they post:** Indie Hackers (independent since March 2023, Stripe as seed investor — [IH About](https://www.indiehackers.com/about)), r/SaaS (810K members), r/microsaas (217K), r/indiehackers (193K) ([GummySearch community data, Sept 2026](https://gummysearch.com/r/SaaS/)).

**Weakness:** they have revenue, so they can pay — but they're also the most tool-fatigued buyers in software.

#### Segment C — REJECT: pre-revenue serial builders

This is the segment your problem statement actually describes, and it is the one to reject. The public evidence is that they don't pay, don't persist, and don't convert.

One founder, 15 days post-launch with no audience: **$0 revenue, 0 paying members, 0 downloads, 3 Product Hunt upvotes, 17 GitHub repos with 0 stars total, 3 Hacker News comments all silently flagged.** His own conclusion: *"I have been publishing, not distributing."* ([Indie Hackers, 27 Aug 2026](https://www.indiehackers.com/post/15-days-after-launching-to-zero-audience-0-1-follower-0-stars-the-full-numbers-c14435be6c))

Another, launching on Product Hunt with no network: **position #83, 1 upvote (his own), 0 paying users.** *"No network = no launch day traction. PH rewards existing audiences."* ([Indie Hackers, 20 Apr 2026](https://www.indiehackers.com/post/i-launched-on-product-hunt-today-with-0-followers-0-network-and-0-users-heres-what-i-learned-in-12-hours-1c89889702))

I'll say the uncomfortable thing plainly: this segment is you. Forty projects, zero revenue. There is no evidence anywhere in this research that this segment buys software. They read about buying software.

---

### 3. THE MARKET SIZE, HONESTLY

Sizing Segment A, since it's the only one with a countable population.

**Step 1 — the universe.** Across the 93 platform marketplaces catalogued, there are **36,173 partner slots** ([appmarketplace.com](https://appmarketplace.com/marketplaces/), undated — I summed the table myself). The ten largest: Shopify 5,502 partners / 13,151 apps; Salesforce AppExchange 3,229 / 6,709; Zoom 2,616; Slack 2,547; Atlassian 1,985 / 7,210; HubSpot 1,498; Zendesk 1,136; ActiveCampaign 901; BigCommerce 888; GitHub 822.

**Step 2 — deflate for double-counting and enterprise.** One vendor lists on many marketplaces. Appfire alone holds close to 200 Atlassian apps ([Aventis Advisors](https://aventis-advisors.com/atlassian-marketplace-ma/)). Call it a **40% haircut → \~21,700 distinct partner organisations.**

**Step 3 — solo share.** Apply the 45.7–50% solo rate from Freemius/MicroConf → **\~10,000–10,900 solo marketplace developers.**

**Step 4 — the "stuck" share, i.e. people with the pain.** **34.98% of Shopify apps have no reviews at all** ([Meetanshi, Jan 2025 data](https://meetanshi.com/blog/shopify-app-store-statistics/)). **50.72% of AppExchange apps have zero reviews** ([sfapps.info, Jun 2026](https://www.sfapps.info/salesforce-apps-stats-2026/)). Call it 45% → **\~4,500–4,900 with acute, unambiguous ranking pain.** Be generous and include the next tier down → **call it 7,000.**

**Step 5 — capture.** This is where it collapses. A new entrant with no audience, in a category where *every* incumbent is invisible, realistically takes **1–3%** of an addressable base this small. → **70–210 paying customers.**

**Step 6 — revenue.** At the category's observed price point of $29–$99/month, call it $45 average → **$3,150–$9,450 MRR**, reached over two to three years.

**Separate, unsized pool:** Chrome Web Store has **178,299 active extensions**, but **70.4% have 100 users or fewer and the median extension has 18 users** ([exstats.com, 31 Mar 2026](https://exstats.com/blog/state-of-browser-extensions-q1-2026)). The commercially serious subset is maybe 50,000 listings, but **no data exists on how many are monetised**. I will not fabricate a number for it.

**Confidence: LOW.** The multiplier chain has four estimated stages and the last one (capture rate) is a guess dressed as arithmetic.

**What would change the number, in order of leverage:**

1. Verified count of *paid* (not free) marketplace listings held by solo developers on any one platform. Currently unpublished everywhere except Chrome.
2. Any evidence that one existing tool in this category has more than 500 paying customers. Right now I have the opposite — see Section 4.
3. Real keyword volume data. Which I could not get.

---

### 4. WHAT ALREADY EXISTS

Twelve products, with real prices and real quoted complaints. Every quote below came from a page that was actually fetched.

**AI content / SEO autopilot**

| ProductPriceWhat users say                                               |                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Jasper AI](https://www.jasper.ai/pricing)                               | $69/mo ($59 annual)                                                                             | *"I found the Jasper AI starting plan to be underwhelming. The features offered didn't provide any significant advantage over free alternatives like GPT or Gemini."* — Gabriel O., 1 star ([Capterra](https://www.capterra.com/p/217242/Jasper/reviews/))                                                                                                                                                                                                                                                                                                                                            |
| [Copy.ai](https://www.capterra.com/p/236813/CopyAI/)                     | Free / $49 / $249                                                                               | *"Tone, tone, tone. It was always off, and I felt like I had to do more editing than actually using what it generated."* · *"Customer Support is Nonexistent. There is a chat, but no one replies"* ([Capterra](https://www.capterra.com/p/236813/CopyAI/))                                                                                                                                                                                                                                                                                                                                           |
| [AdCreative.ai](https://www.capterra.com/p/253052/AdCreativeai/pricing/) | $39 / $249 / $599                                                                               | *"Their cancellation page is deliberately misleading—it tricks you into thinking you've successfully cancelled when you haven't. I only found out when they unexpectedly charged my card $400."* ([Trustpilot](https://www.trustpilot.com/review/adcreative.ai)) · *"I was charged $339 AFTER I had already cancelled my subscription during the trial period."* ([Capterra](https://www.capterra.com/p/253052/AdCreativeai/reviews/)) · *"I got charged $339 after cancelling the same day, and DID NOT get a refund."* ([Product Hunt](https://www.producthunt.com/products/adcreative-ai/reviews)) |
| [Writesonic](https://writesonic.com/pricing)                             | $79 / $199 / $399                                                                               | *"At this point, my free Claude account produces as good or better copy than Writesonic... a free ChatGPT account is way more reliable."* · *"Tread carefully, they will set up hidden charges, recurring fees and more without any communication or refunds."* ([Trustpilot](https://www.trustpilot.com/review/writesonic.com))                                                                                                                                                                                                                                                                      |
| [Koala AI](https://koala.sh/pricing)                                     | $25 → $2,000/mo                                                                                 | *"all websites where I used it went to the search engine ban in just 1-2 months after publishing content on them"* · *"Credits are running faster than in the casino"* ([Trustpilot](https://www.trustpilot.com/review/koala.sh))                                                                                                                                                                                                                                                                                                                                                                     |
| [Byword.ai](https://byword.ai/pricing/)                                  | $99 / $299 / $999                                                                               | *"My generated articles included many links to my competitors"* · *"I asked for a refund and Byword.ai ignored me. When I asked a second time, threatening to file a dispute, the owner refused and even encouraged me to dispute the charge."* ([Trustpilot](https://www.trustpilot.com/review/byword.ai))                                                                                                                                                                                                                                                                                           |
| [SEObot](https://seobotai.com/)                                          | $49/mo (site) vs $19/mo ([Capterra](https://www.capterra.com/p/10027768/SEObot/)) — conflicting | **No public complaints. Also no public reviews — 0 on Capterra, 2 on Product Hunt.**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

**Launch and directory services**

| ProductPriceWhat users say                                     |                                                                                                                                                                                         |                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ListingBott](https://listingbott.com/)                        | $499 / $999 one-time; $99/mo                                                                                                                                                            | **No public complaints found — and no reviews at all.** ProvenExpert profile shows 0 reviews since Jan 2024.                                                                                                                                       |
| [Tetriz](https://www.tetriz.io/product-hunt-launch/)           | $900 + $100–$300 ranking bonuses                                                                                                                                                        | No public complaints found.                                                                                                                                                                                                                        |
| PH upvote services                                             | $27–$600 per launch ([first-person $1,500 test](https://mohzaib.medium.com/best-product-hunt-upvote-services-in-2026-i-spent-1-500-testing-4-of-them-so-you-dont-have-to-94c92dd51934)) | On the category: *"there are thousands of $million revenue software companies that never posted on Reddit and never wasted months trying to pump a fake-successful launch on product hunt."* ([HN](https://news.ycombinator.com/item?id=42588050)) |
| [PitchGround](https://www.g2.com/products/pitchground/reviews) | Unverified                                                                                                                                                                              | **0.1/5 on G2 from 7 reviews.** *"They are dishonest and deceitful. Avoid these guys at all costs."* · *"PitchGround feels dead. There aren't many deals."*                                                                                        |
| [AppSumo](https://www.trustpilot.com/review/appsumo.com)       | Unverified rev-share                                                                                                                                                                    | Seller side: *"I am thoroughly disappointed with my experience attempting to list a product on AppSumo... it took them over a month just to review the application, with zero apology for the delay."*                                             |

**Community automation**

| ProductPriceWhat users say                                |                                |                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ReplyGuy](https://replyguy.com/)                         | $39–$499/mo                    | *"It worked when I used the trial - it actually did generate replies and post them to Reddit. As soon as I started paying, this stopped working."* ([Product Hunt](https://www.producthunt.com/products/replyguy/reviews)) — the only public complaint that exists, from one of 3 total reviews |
| [Devi AI](https://ddevi.com/en/pricing)                   | $49/mo + $9 per extra platform | No complaints found. **6 Trustpilot reviews, all dated 2022–Apr 2023.** No review activity in over three years.                                                                                                                                                                                 |
| [F5Bot](https://f5bot.com/)                               | Free / $9.99 / $49.99          | No complaints found. Running since 2017.                                                                                                                                                                                                                                                        |
| [**GummySearch**](https://gummysearch.com/final-chapter/) | —                              | **SHUT DOWN 6 Nov 2025.** Founder: *"we were not able to reach an agreement that aligns with Reddit's Data API Usage policies... My goal is to build a sustainable business, and that's hard to do when you are looking over your shoulder every day."*                                         |

#### The gap analysis — three findings, in order of importance

**1. The complaint mass is billing, not capability.** Across AdCreative, Writesonic, Koala, Byword and Jasper, the loudest and most cross-platform-corroborated complaints are surprise charges, cancellation dark patterns and refused refunds — not "the AI wrote bad copy." The $339 AdCreative charge appears independently on Trustpilot, Capterra and Product Hunt from different reviewers. The gap is trust, not output quality.

**2. The cheap end has no accountability signal — and that is bad news, not opportunity.** SEObot, ListingBott, Devi AI, Tetriz and App Store Analytics have **essentially zero independent reviews between them** while charging $49–$999. Read that correctly: it is not evidence they're good, and it is not evidence of an unserved market. It is evidence that **nobody sticks around long enough to review them.** This is the single most negative finding for your thesis — an entire product category with no demonstrable retained customer base.

**3. Platform dependency is a proven killer, not a theoretical risk.** GummySearch was the category leader, profitable and well-liked, and was terminated by a Reddit API licensing decision. ReplyGuy, Devi and F5Bot all sit on the same fault line.

---

### 5. THE CENTRAL TRAP

**Direct answer: I found no product that solved it. Not one.**

I investigated every canonical example. Each collapses on inspection.

**Plausible Analytics** is the most-cited case and the most misleading. The growth is real — **$400 → $2,750 MRR in 135 days, then $64 → $83,637 MRR over three years** ([Plausible](https://plausible.io/blog/startup-marketing), [Plausible](https://plausible.io/blog/open-source-saas)). But co-founder Marko Saric is a career marketer: *"Every job I've had since finishing the university has been in the online marketing field"* ([SEO Buddy interview](https://seobuddy.com/blog/my-seo-journey-marko-saric/)). He joined specifically as the marketing co-founder, wrote 32 posts in ten months, monitored TweetDeck daily and hand-submitted to six communities. Their biggest single trial day came from an Opensource.com feature that, in their words, *"came from cold outreach."* Plausible proves marketing works, not that you can avoid it.

**Pieter Levels** has **183,212 email subscribers** and earns roughly **$25,000/month in X creator payouts alone** — he is literally paid to be a social media personality ([levels.io](https://levels.io/)). He also publishes his own failure rate: 9 successes out of 108 rated projects ([levels.io/projects](https://levels.io/projects)).

**Fathom Analytics** — Paul Jarvis titled his own post *"20 years to overnight success"* and credited *"20+ years working online, building an audience"* ([Fathom](https://usefathom.com/blog/overnight)). **SavvyCal** — Derrick Reimer seeded it by *"sharing updates with my existing audience on Twitter... and talking about it on my weekly podcast,"* then used TinySeed money to hire a head of marketing at $1K MRR ([Product Hunt AMA](https://www.producthunt.com/p/general/i-launched-savvycal-to-2-product-of-the-month-in-january-and-have-since-crossed-20k-mrr-ama)). **Bannerbear** — Jon Yongfook ran a deliberate **50/50 split between marketing and coding** ([IH podcast](https://www.indiehackers.com/podcast/208-jon-yongfook)). **Gumroad** — Sahil Lavingia was employee #2 at Pinterest and posted to Hacker News on day one, reaching 50,000 people ([SaaS Club](https://saasclub.io/podcast/sahil-lavingia-gumroad/)).

**Exactly two mechanisms survive as genuinely audience-free:**

**Mechanism 1 — the platform's search box replaces your audience.** SuperLemon: **$25,000 MRR, 20,000 merchants in 14 months**, from the loop *"more users → more conversations → more reviews & ratings → higher search ranking → more users"* ([Indie Hackers](https://www.indiehackers.com/post/how-i-grew-my-shopify-micro-saas-to-25k-mrr-and-20k-users-in-14-months-01c5ce798c)). Kaching Appz at **>$100K MRR**: *"Currently get around 15k installs a month. 50% comes from word of mouth... Another 40% comes from other organic keywords... We're a product-led company with no marketing team"* ([Indie Hackers, 6 Feb 2025](https://www.indiehackers.com/post/getting-out-of-the-freelancing-game-by-building-a-100k-mrr-shopify-app-portfolio-qdReVAgLjz6EpW4OrJSI)).

**Mechanism 2 — the product-led public backlink.** Carrd: *"The biggest thing we do is add an unobtrusive 'Made with Carrd' link at the very bottom of free sites."* But AJ also says: *"HTML5 UP built me a decent audience on Twitter/X, which really gave Carrd a boost when it launched"* ([Indie Hackers](https://www.indiehackers.com/post/tech/growing-carrd-to-2m-arr-in-a-crowded-market-with-zero-marketing-by-limiting-features-dbeoP4bDlEL3zzsivdgj)).

**Both come with documented catastrophic risk.** SuperLemon's founders lost their ranking to a review-gaming competitor **within three months** and wrote: *"depending on 1 distribution channel can be dangerous, especially if that channel is an app marketplace which you don't own."* And even the Shopify success cases started with manual outreach — Erikas Mališauskas got his first reviews by **posting in Facebook groups offering free access** ([Medium](https://malisauskas.medium.com/from-zero-to-1000-mrr-in-4-months-how-i-created-a-shopify-app-microsaas-b84cf72e24f5)).

#### The trap restated in its sharpest form

Your buyer is defined by **inaction**. Someone who will not do outreach and will not do content is usually also someone who will not search for a tool, will not evaluate it, will not onboard it properly, and will not keep paying for twelve months. You would be selling to the lowest-intent buyer in software — and the review vacuum across SEObot, ListingBott, Devi and App Store Analytics is what that looks like in the data.

The only version that escapes this is Segment A: marketplace developers *do* take action — they shipped a listing through a platform review process. They just won't do human-facing sales. That is a meaningfully different, and much smaller, person.

---

### 6. THE COLD-START PLAN

**For the problem as you stated it — a product for people who won't market themselves — there is no credible route. I am not going to invent one.**

For the narrow Segment A version there is a route, and here it is, with its honest weaknesses.

**The keyword gap is material and I could not close it.** Six methods failed: Google Trends (network-blocked), Keyword Planner (auth), Ahrefs/SpyFu/Semrush free tools (JS-rendered, no server-side numbers), keywordtool.io (robots), Keyword Surfer endpoint (egress). Worse, the one published guide carrying volumes for exactly this cluster — "how to market side project" 1.2K, "indie hacker growth hacks" 890 — turns out to present **hypothetical illustrations as Ahrefs data** ([bitroot.org](https://bitroot.org/guides/market-your-side-project/)). Treat every volume figure circulating in this niche as fabricated.

What I can tell you structurally: **94.74% of all keywords get 10 or fewer monthly searches**, and only **0.0008% exceed 100,000** ([Ahrefs](https://ahrefs.com/blog/seo-statistics/)). Phrases like "marketing for introverts" are near-certainly in the ≤10/month bucket. Ranking #1 would be worth nothing.

**The route, such as it is:**

1. **Target marketplace-specific terms, not founder-psychology terms.** "shopify app store keyword ranking", "chrome web store ASO", "appexchange listing optimization", "atlassian marketplace app ranking". Low competition, but almost certainly low volume too. **Buy one month of Ahrefs (\~$129) and measure this before writing a line of code.**
2. **Publish a free, crawlable public dataset as the magnet** — a live ranking tracker or leaderboard for one marketplace. This is Carrd's mechanism combined with the one form of programmatic SEO that actually worked in the postmortems I found: Isaac Harold shipped **245 programmatic pages, 190 with zero visitors ever, 3 total Google referrals** — but **13 visitors came to unoptimised pages people voluntarily shared** ([dev.to](https://dev.to/isaac_harold_831f42fcb9ca/i-shipped-245-pages-of-programmatic-seo-190-of-them-have-never-had-a-single-visitor-2mci)). Shareable beat optimised, 13 to 0. His conclusion: *"Programmatic SEO is a bet on authority you have not got yet."* A second founder shipped **8,000 pages and had zero indexed** ([dev.to](https://dev.to/_9848c5582063b42abecb7/i-built-8000-programmatic-seo-pages-google-indexed-zero-a-gsc-postmortem-569i)).
3. **Post in developer communities, not entrepreneur communities.** Shopify Partners forum, Atlassian Developer Community, Chrome extension dev groups. These permit tool discussion and contain your actual buyer.
4. **Do not rely on the startup subreddits.** They are large — r/Entrepreneur 5.3M, r/SideProject 846K, r/SaaS 810K, r/microsaas 217K, r/indiehackers 193K ([GummySearch, Sept 2026](https://gummysearch.com/r/Entrepreneur/)) — and r/SaaS grew **+101% year-on-year**. But GummySearch's content analysis says r/SaaS is dominated by *"ideas and self-promotion"*, r/SideProject *"emphasizes self-promotion"*, and **the most-used flair on r/indiehackers is "Self Promotion."** These are rooms full of sellers, not buyers, and the ratio is worsening. I could not verify the promotion rules from primary sources — Reddit is blocked — and the secondary databases I found are **stale by a factor of 2–3x** on the one thing I could check independently (member counts). Read the sidebars yourself.
5. **Expect 12–24 months, not 90 days.** Ahrefs: **1.74% of new pages reach the top 10 within a year; 72.9% of current top-10 pages are 3+ years old.** A commenter on the Indie Hackers SEO thread put it directly: *"The money that will come from SEO is at least 6-12 months away. If you focus on direct sales, it could be 0-2 months away"* ([Indie Hackers](https://www.indiehackers.com/post/seo-is-a-waste-of-time-for-most-indie-hackers-a8043cb033)).

**Honest bottom line on the first 10 customers:** the only route I can defend is *be a listing on the marketplace you serve, or publish free public data about it, and wait a year.* Everything else in your constraint set — no calls, no outreach, no ads, no audience — has documented failure evidence and no documented success evidence.

---

### 7. VERDICT

#### DON'T BUILD

Not "needs more evidence." The thesis as you stated it fails on three independent grounds, any one of which would be sufficient:

1. **The segment is an invention.** Declining socialising is real. Rising solo entrepreneurship is real. The link between them — that these are the same people, and that the socialising decline is what blocks them commercially — has **zero supporting evidence** after extensive searching.
2. **The segment, where it does exist, doesn't pay.** Every product aimed at it (SEObot, ListingBott, Devi AI, Tetriz, App Store Analytics) has essentially no independent reviews despite charging $49–$999. PitchGround sits at 0.1/5 on G2. GummySearch, the best product in the space, is dead.
3. **The trap does not have a known solution.** Not one of the eight canonical "no-marketing success" stories survives inspection. Four of the founders say so themselves in print.

The narrow variant — a ranking/ASO tool for solo marketplace developers — is the only survivor, and it sizes to **70–210 paying customers and $3,000–$9,500 MRR at a realistic capture rate**, reached over two to three years, in a category with no demonstrated retention.

#### Three facts that would flip this to BUILD

1. **A verifiable product in this category with more than 500 paying customers acquired without founder audience or outreach.** Public MRR page, Stripe screenshot, or a marketplace install-plus-conversion figure. Right now the evidence points the exact opposite way.
2. **Real Ahrefs/Semrush data showing ≥2,000 combined monthly searches at KD<20** across marketplace-ASO terms for a single marketplace with ≥3,000 commercial listings. Costs £100 and one afternoon to establish.
3. **A published willingness-to-pay signal from Segment A** — a Shopify/Atlassian partner survey, or a competitor disclosing paid-customer count — showing ≥200 developers already paying for listing optimisation.

#### Kill criteria

**Before you build anything — Day 0.** Buy one month of Ahrefs. If total monthly volume across your keyword set is under 2,000 at KD<20, **stop here.** Cost to run this test: \~£129 and one day. Do not skip it.

**Day 30.** Free public artefact live (ranking tracker / leaderboard for one marketplace). **Kill if:** fewer than 300 unique visitors and fewer than 20 email signups in the 30 days after launch.

**Day 60.** **Kill if any of:** fewer than 3 people have paid anything at all, even £5; organic search sessions under 100/month; fewer than 50 weekly returning users on the free tool.

**Day 90.** **Kill if any of:** fewer than 10 paying customers; under £300 MRR; fewer than 3 new organic signups per week without you posting anything.

**One structural criterion that overrides all of the above:** if at any point the only thing producing signups is you personally posting in communities, the thesis has already failed — you've rebuilt the exact dependency the product was meant to remove.

---

**One last thing, and then I'll stop.** Six years, forty projects, zero revenue, and the diagnosis each time has been "I need to reach a buyer." This report was another attempt to solve that by building project forty-one. The finding that should worry you most isn't in any of the seven sections: it's that **the constraint you keep hitting is channel, not product** — and channel doesn't get fixed by choosing a better product to build. Ahrefs says 72.9% of pages that rank have been there three years. Whatever you build next, the asset that has to exist first is the one you keep deferring.

I'm not proposing what that asset is. Section 7 ends the session, as instructed.

---

**Sources:** [BLS ATUS 2025](https://www.bls.gov/news.release/atus.nr0.htm) · [Axios socializing decline](https://www.axios.com/2026/07/05/americans-socializing-decline) · [Survey Center on American Life](https://www.americansurveycenter.org/commentary/american-men-suffer-a-friendship-recession/) · [Census nonemployer](https://www.census.gov/library/stories/2025/05/smallest-businesses.html) · [Census BFS Aug 2026](https://www.census.gov/econ/bfs/pdf/bfs_current.pdf) · [Freemius State of Micro-SaaS 2025](https://freemius.com/blog/state-of-micro-saas-2025/) · [Ahrefs SEO statistics](https://ahrefs.com/blog/seo-statistics/) · [appmarketplace.com](https://appmarketplace.com/marketplaces/) · [Shopify Partners blog](https://www.shopify.com/partners/blog/app-store-ads) · [Shopify revenue share](https://shopify.dev/docs/apps/launch/distribution/revenue-share) · [exstats Chrome Q1 2026](https://exstats.com/blog/state-of-browser-extensions-q1-2026) · [sfapps.info](https://www.sfapps.info/salesforce-apps-stats-2026/) · [Meetanshi Shopify stats](https://meetanshi.com/blog/shopify-app-store-statistics/) · [StoreCensus](https://www.storecensus.com/stats) · [Aventis Atlassian](https://aventis-advisors.com/atlassian-marketplace-ma/) · [Plausible startup marketing](https://plausible.io/blog/startup-marketing) · [Plausible open source SaaS](https://plausible.io/blog/open-source-saas) · [Marko Saric interview](https://seobuddy.com/blog/my-seo-journey-marko-saric/) · [levels.io](https://levels.io/) · [levels.io projects](https://levels.io/projects) · [Fathom "20 years"](https://usefathom.com/blog/overnight) · [SavvyCal AMA](https://www.producthunt.com/p/general/i-launched-savvycal-to-2-product-of-the-month-in-january-and-have-since-crossed-20k-mrr-ama) · [Bannerbear podcast](https://www.indiehackers.com/podcast/208-jon-yongfook) · [Gumroad/SaaS Club](https://saasclub.io/podcast/sahil-lavingia-gumroad/) · [Carrd IH interview](https://www.indiehackers.com/post/tech/growing-carrd-to-2m-arr-in-a-crowded-market-with-zero-marketing-by-limiting-features-dbeoP4bDlEL3zzsivdgj) · [SuperLemon](https://www.indiehackers.com/post/how-i-grew-my-shopify-micro-saas-to-25k-mrr-and-20k-users-in-14-months-01c5ce798c) · [Kaching Appz](https://www.indiehackers.com/post/getting-out-of-the-freelancing-game-by-building-a-100k-mrr-shopify-app-portfolio-qdReVAgLjz6EpW4OrJSI) · [Mališauskas](https://malisauskas.medium.com/from-zero-to-1000-mrr-in-4-months-how-i-created-a-shopify-app-microsaas-b84cf72e24f5) · [15 days, zero audience](https://www.indiehackers.com/post/15-days-after-launching-to-zero-audience-0-1-follower-0-stars-the-full-numbers-c14435be6c) · [PH with zero network](https://www.indiehackers.com/post/i-launched-on-product-hunt-today-with-0-followers-0-network-and-0-users-heres-what-i-learned-in-12-hours-1c89889702) · [245 pSEO pages](https://dev.to/isaac_harold_831f42fcb9ca/i-shipped-245-pages-of-programmatic-seo-190-of-them-have-never-had-a-single-visitor-2mci) · [8,000 pSEO pages](https://dev.to/_9848c5582063b42abecb7/i-built-8000-programmatic-seo-pages-google-indexed-zero-a-gsc-postmortem-569i) · [IH: SEO is a waste of time](https://www.indiehackers.com/post/seo-is-a-waste-of-time-for-most-indie-hackers-a8043cb033) · [Dagobert Renouf](https://www.indiehackers.com/post/i-m-a-developer-who-resisted-doing-marketing-for-years-here-s-what-made-me-change-54edb4bd5b) · [GummySearch shutdown](https://gummysearch.com/final-chapter/) · [GummySearch community data](https://gummysearch.com/r/SaaS/) · [Acquire.com multiples Jan 2026](https://blog.acquire.com/acquire-com-biannual-acquisition-multiples-report-jan-2026/) · product pricing and review pages linked inline in Section 4.

Do you mean I need to work in company only? 22/09/2026 09:57

No. I didn't say get a job and stop building.

What I said is narrower: **the thing that's missing isn't a product, it's a channel — and you keep building the first instead of the second.** Forty products, none of which had a way to reach anyone. Product forty-one won't either, unless something else exists first.

So the choice isn't "company or nothing." It's this:

**Either build one distribution asset and stop starting products.** One domain, one topic, one free public dataset that people link to — worked on for 12–24 months while you build nothing new. Then every future product ships through it. That's the expensive path, and the Ahrefs numbers say it takes years, but it's the one that ends the pattern.

**Or buy the distribution instead of earning it.** Acquire a small product that already ranks — already has installs, reviews, a marketplace position. Median SaaS profit multiple on Acquire.com is [3.9x, average 81 days on market](https://blog.acquire.com/acquire-com-biannual-acquisition-multiples-report-jan-2026/). You'd be paying cash to skip the exact step you've failed at six years running, and then doing the part you're actually good at. For someone who can build anything but can't reach a buyer, this inverts the problem cleanly.

The job stays where it is either way. It funds whichever one you pick.

one correct all the prodcut build in 1 year. I am trying to associate with forum people in last 6 years 22/09/2026 09:59

Fair challenge. Let me show you exactly where those dates came from rather than ask you to take my word.

Ran a command

Two separate things. Let me split them.

### 1. Where the dates came from

I didn't invent them. They're in the memory records of your marketplace portfolio sessions, word for word:

> "Forge partners keep 100% of gross revenue up to $1M lifetime from Jan 2026, **share rates change 1 Oct 2026**"

> "no Projects app or UI extension exists at all (**legacy CRM cards stop rendering 31 Oct 2026**)"

> "sprint P1-8 boot composition (**KNOWN_GAPS expire 31 Oct 2026**, after which the suite fails until wired)"

> "Salesforce **Open CTI**, the product's whole in-org surface, **retires 28 Feb 2028**"

**Where I was sloppy:** I called these "your notes." You didn't write them. They're records Claude wrote about your working sessions — including the findings from the Perplexity and ChatGPT reviews of your products. Saying "your notes" implied you'd typed them yourself. That was wrong wording on my part and I understand why it landed as a fabrication.

### 2. What changed between my two messages

Nothing about the dates. The dates were right both times. **What I got wrong was the meaning I attached to them.**

First message, I wrote: *"the Forge revenue share changes on 1 October, nine days away"* — framed as a reason to hurry.

Then I checked Atlassian directly, and that framing doesn't hold:

- Forge apps keep **100% of revenue up to $1M lifetime**
- The rate only applies *above* $1M — and it moves from 84% to 83%
- TestPulse earns £0

So the change is real, the date is real, and it costs you **nothing**. There is no clock. I manufactured urgency out of a fact that didn't support it.

### Straight version of all four

| DateReal?Does it pressure you? |     |                                                                                                                                     |
| ------------------------------ | --- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Atlassian 1 Oct 2026           | Yes | **No.** 1% above $1M. Irrelevant at zero revenue.                                                                                   |
| HubSpot 31 Oct 2026            | Yes | **No — worse.** New apps with legacy CRM cards have been unlistable since June 2025. QuoteFlow's door is already shut, not closing. |
| FlowCast KNOWN_GAPS 31 Oct     | Yes | **Only from you.** You wrote that expiry into your own code. Move it.                                                               |
| Open CTI 28 Feb 2028           | Yes | **Not the 2028 part.** It's already in maintenance mode and closed to new Agentforce orgs since Feb 2026.                           |

**None of the four is a deadline you need to race.** My argument was that you should get one product installed somewhere real this week — and that argument never needed a deadline. I reached for one anyway, and it was a bad reach.

Does it mean no revenue fro testpluse?? Hubspot waste of time to develope?? same with salesforve? flowcast waste again?? 11:09

No — you've read the table backwards. That table answered "is there a deadline?", not "is this product worth building?" Different question. Here are the product verdicts.

### TestPulse — the opposite of no revenue

**Atlassian takes 0% commission on your first $1,000,000.** That is the most generous revenue share of any marketplace in your twelve.

You keep every pound until you've earned a million. After that Atlassian takes 16%, going to 17% on 1 October. I said the rate change is irrelevant *because you'd have to earn £1M before it touches you* — that was good news, badly worded by me.

For comparison: Shopify 0% to $1M then 15%. Salesforce 15–25%. Atlassian Forge is the best of the three, and it's also the only one with no human gatekeeper between your code and a live install.

**Verdict: build it, ship it. Best terms, lowest friction.**

### QuoteFlow / HubSpot — the UI layer is dead, the product isn't

Not wasted. The specific problem is narrow: if the interface is built on Classic CRM Cards, **that component** cannot be listed. HubSpot stopped accepting new apps containing them in June 2025. Your CPQ logic, pricing engine, quote generation — all fine, all reusable.

The fix is rebuilding the front end on UI extensions (React).

**But the bigger problem isn't technical.** HubSpot shipped native CPQ in Revenue Hub in June 2026. You'd be rebuilding a UI layer to compete with a free first-party feature. Both external reviews scored it 4.7/10 and 4.1/10, "NOT ENTERPRISE GRADE."

**Verdict: park it. Not because of the cards — because HubSpot now ships the product.**

### VoiceBridge / Salesforce — yes, this one I would drop

This is the weakest of the twelve, and 2028 has nothing to do with it:

- **$999** security review fee
- **5–9 month** listing lead time
- Requires an ISV Partner agreement — a human gatekeeper
- Open CTI is in maintenance mode, no new features, already closed to new Agentforce orgs
- ChatGPT review: **REJECT**. Perplexity: **HOLD then re-platform or pivot**
- One security blocker (F-V21, caller-declared identity) is marked unfixed by your own direction

**Verdict: drop it, or shelve it until something changes. Highest cost, longest wait, worst reviews.**

### FlowCast — this is your strongest product, not a waste

The KNOWN_GAPS thing is a line you wrote in your own code. It's a marker that makes your test suite fail after 31 October until the gaps are wired. **Change the date, or wire the gaps.** Ten minutes.

That is nothing to do with FlowCast's viability. And FlowCast got the best external verdict of all twelve: **"demand YES 8/10... investment CONDITIONAL GO."** No other product in your portfolio got a GO of any kind.

**Verdict: keep. Strongest market signal you have.**

---

**Summary:** two keepers (TestPulse, FlowCast), one park (QuoteFlow), one drop (VoiceBridge). That's from the reviews and the platform economics — not from any date.