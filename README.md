# claude-app-store-optimization-skill

A Claude Code skill for improving mobile app discoverability and conversion through structured App Store Optimization (ASO) workflows.

## Overview

This skill supports research, listing optimization, keyword planning, creative asset review, localization, and measurement for Apple App Store and Google Play listings.

ASO work should be based on accurate product information and real performance data. Keyword repetition or unsupported claims can damage trust and listing quality.

## Main Capabilities

- Research relevant app keywords.
- Review competitor positioning and metadata.
- Optimize app titles and descriptions.
- Plan subtitles and promotional text.
- Evaluate category and keyword choices.
- Improve icon, screenshot, and preview presentation.
- Plan localization across markets.
- Review user feedback and ratings.
- Estimate experiment requirements.
- Build launch and iteration checklists.

## Installation

```bash
git clone https://github.com/Brajesh31/claude-app-store-optimization-skill.git ~/.claude/skills/app-store-optimization
```

The repository includes offline Python utilities. Review their command-line options and test requirements before use.

## Usage

Invoke the skill for app listing research or optimization:

```text
/app-store-optimization
```

Provide the app category, target audience, target markets, current listing, product features, and available analytics.

## Recommended ASO Workflow

1. Define the target audience and market.
2. Review the current app listing.
3. Research relevant keywords and competitors.
4. Prioritize keywords by relevance and intent.
5. Improve title, subtitle, and description.
6. Review icon and screenshot messaging.
7. Plan localization where it supports the target market.
8. Validate platform character limits.
9. Measure impressions, page views, installs, and conversion.
10. Iterate based on reliable performance data.

## Utility Scripts

The repository includes offline utilities for:

- Keyword triage.
- Metadata character-limit validation.
- Competitor metadata comparison.
- Heuristic ASO scoring.
- A/B test sample-size estimation.
- Localization limit checks.
- Review sentiment triage.
- Launch checklist generation.

These scripts operate on supplied input data. They do not fetch live store search volume, competitor rankings, or official analytics.

## Running Tests

```bash
python -m unittest discover -s tests -v
```

## Quality Checklist

- Listing claims match the actual app.
- Keywords are relevant to user intent.
- Titles and descriptions respect platform limits.
- Screenshots show real product functionality.
- Localization is reviewed by fluent speakers where possible.
- Competitor comparisons use current, comparable data.
- Experiments have defined metrics and decision criteria.
- Changes are measured over a sufficient period.

## Repository Contents

- `SKILL.md`: Main ASO workflow.
- `scripts/`: Offline analysis and validation utilities.
- `tests/`: Utility tests.
- `README.md`: ASO workflow and usage guide.

## Practical Principle

A higher ranking is not the only goal. Optimize for qualified discovery and installs from users who are likely to understand and value the app.
