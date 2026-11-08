# App Store Optimization

## Overview

This repository contains a Claude skill focused on app store optimization (ASO). It provides a structured workflow for improving an app's store listing, discoverability, and conversion performance.

## What It Covers

- App listing and positioning considerations.
- Keyword and metadata planning.
- Creative assets and conversion-focused presentation.
- Measurement, iteration, and performance review.

## Getting Started

1. Read `SKILL.md` to understand the workflow and scope.
2. Install the skill in the skills directory supported by your Claude environment.
3. Provide the app category, target audience, markets, and current listing details.
4. Follow the skill's process to assess and improve the listing.
5. Measure changes over time and validate impact using reliable store analytics.

## Practical Guidance

Avoid keyword stuffing and unsupported claims. Keep the listing accurate, localized where appropriate, and aligned with the actual app experience. Store ranking and conversion behavior can change, so review current platform guidance.

## License

MIT. See [LICENSE](LICENSE).

## Utility scripts

Added eight offline utilities under `scripts/`: keyword triage, metadata character-limit validation, competitor metadata comparison, ASO heuristic scoring, A/B sample-size estimation, localization limit checks, review sentiment triage, and launch checklist generation. These scripts work only from supplied input data. They do not fetch live store search volume, competitor rankings, or official analytics. See each script's `--help` output for usage.
