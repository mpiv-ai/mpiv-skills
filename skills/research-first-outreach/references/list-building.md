# List building

The agent builds the list. The human approves it. Source two to three times the number you plan to email.

## Record fields

One row per person. Keep it in a spreadsheet, a CRM, or a markdown table. Nothing here is optional.

| Field | Rule |
|---|---|
| first_name, last_name | From the site's about or team page. No name, no row. |
| email | From the site. Prefer a personal address over info@ or hello@. If only a form exists, note `form-only` and rank last. |
| company | As they write it. |
| site | Home page URL. |
| role | Their words: "Fractional COO", "Founder and Principal Consultant". |
| workflow_page | The URL of the page that describes their repeatable process. |
| observation | One sentence, written while the page is open. See rules below. |
| segment | Role and industry, so cohorts can be mixed on purpose. |
| status | identified, drafted, sent, replied, booked, closed. |
| first_sent_at, replied_at, booked_at | Timestamps. |

## Search queries

Run each role against each industry the user cares about. Add the process words; they filter for people who publish how they work.

Roles: fractional COO, fractional CFO, fractional CTO, fractional CMO, fractional product manager, fractional product leader, operations consultant, HR consultant, compliance consultant, revenue-cycle consultant, practice-management consultant, independent product consultant.

Process words: "our process", "how we work", "assessment", "diagnostic", "readiness", "phase", "engagement", "interim", "coverage", "health check", "audit", "scorecard".

Examples:

- `"fractional COO" "our process" site:*.com -jobs -hiring`
- `"fractional CFO" "financial assessment" -site:linkedin.com`
- `"interim product" "parental leave" consultant`
- `"fractional CTO" "readiness assessment"`
- `"practice management" consultant "startup" medical -site:linkedin.com`

Skip LinkedIn, job boards, and directory sites in results. You want the person's own domain.

## Qualification checklist

Open the site. Read the services page and the about page. Then answer yes to all four or drop the row.

1. Is there a named human who owns the practice?
2. Is there a page that describes a repeatable client workflow in their own words?
3. Is there an email address, or at minimum a form, on the site?
4. Would the founder read and answer this mail personally?

Drop if: an agency with a sales team, a template site with no process content, a site that has not been touched in years, or someone the user already knows.

## The observation sentence

Write it while the page is open. One sentence. It must:

- Name one specific thing from their site: a named assessment, a phase, a number, an artifact, an offer.
- Start with "I saw that", "I noticed", or "Your".
- Contain no praise and no adjectives about them.
- Be true. If you are not sure the site says it, do not write it.

Bad: "I love the work you're doing with startups."
Good: "I saw that Service Design Collective assessed more than 150 public-facing digital forms across over 20 platforms for the City of Boston."

## Prompt to hand an agent

```
Build a research-outreach list for me.

Target: {who, in one sentence, e.g. "independent and fractional consultants in the US who publish a named, repeatable client process on their own website"}.
Industries: {list}.
Count: find {N x 3} candidates so that {N} survive qualification.

For each candidate, open the site, read the services and about pages, and produce one row with: first_name, last_name, email, company, site, role, workflow_page, observation, segment.

Qualification: named human owner; a page describing a repeatable workflow in their own words; an email on the site; the owner would read the mail. Drop agencies with sales teams, template sites, dead sites, and anyone on this exclusion list: {names}.

Observation sentence rules: one sentence, starts with "I saw that", "I noticed", or "Your", names one specific artifact, phase, number, or offer from their site, no praise, no adjectives about them, only claims the site makes.

Output a markdown table. Then list the candidates you dropped and why, in one line each.
```
