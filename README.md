# OpenClaw ShrimpCard

Turn real agent evidence into a validated public card bundle: self-intro JSON, share-card JSON, a real 8-bit character image, and final screenshot-friendly HTML.

## Why this project

Most "agent profile" demos stop at a prompt, a placeholder image, or some generic copy. OpenClaw ShrimpCard is stricter:

- it starts from evidence instead of vibes
- it rejects sample/fixture identity leakage
- it forces validation before public copy ships
- it requires a real attached image before final HTML renders

This makes it useful when you want an agent card that is actually publishable, not just mockable.

## What it produces

Given live `agent-evidence/1.0`, the pipeline produces:

1. `agent-self-intro-submission/1.0`
2. `share-card/1.0`
3. a real 8-bit PNG character image
4. final HTML card output for sharing or screenshot export

Canonical flow:

```text
agent-evidence -> self-intro submission -> share-card -> final image -> selfie-card.html
```

## Showcase

Generated project mascot:

![OpenClaw ShrimpCard pixel character](docs/showcase/openclaw-shrimpcard.png)

Persistent showcase assets copied out of `output/`:

- Chinese card HTML: [docs/showcase/selfie-card.zh.html](docs/showcase/selfie-card.zh.html)
- English card HTML: [docs/showcase/selfie-card.en.html](docs/showcase/selfie-card.en.html)
- Final share-card bundle: [docs/showcase/share-card.final.json](docs/showcase/share-card.final.json)

These files are intentionally stored under `docs/showcase/` so they remain available even if `output/` is deleted.

## Core strengths

- Evidence-backed identity extraction. The workflow is designed to describe repeated observed behavior, not hypothetical ability.
- Hard validation gates. Field length, generic wording, mascot rules, image constraints, and final-bundle checks are enforced by scripts.
- Complete artifact chain. The repository covers prompts, schemas, validation, image attachment, and final rendering in one place.
- Share-ready output. The final HTML removes preview-only internals and is suitable for direct presentation.

## Repository structure

```text
agents/       interface metadata
assets/       card template and bundled visual assets
examples/     smoke-test fixtures only, not live inputs
references/   evidence extraction guidance
schemas/      JSON schemas
scripts/      prompt builders, validators, converters, renderers
docs/showcase persistent demo assets for README and GitHub visitors
```

## Quick start

Install the only required dependency:

```bash
pip install -r requirements.txt
```

Then run the flow with your own live evidence:

```bash
python3 scripts/build_memory_search_prompt.py path/to/agent-context.json --lang zh
python3 scripts/build_submission_prompt.py path/to/agent-evidence.json --lang zh
python3 scripts/validate_self_intro_submission.py path/to/submission.json
python3 scripts/submission_to_share_card.py path/to/submission.json --out share-card.json
python3 scripts/build_image_task_prompt.py path/to/submission.json --out image-task.txt
python3 scripts/attach_generated_image.py share-card.json --image-file path/to/final.png
python3 scripts/validate_final_bundle.py share-card.json
python3 scripts/render_card_html.py share-card.json --lang zh --out selfie-card.html
```

## Smoke test

The repo includes a current-flow smoke test:

```bash
bash scripts/smoke_test_current_flow.sh
```

It verifies that the fixture-based example path can still generate prompts, a share card, an attached-image bundle, and both Chinese and English HTML outputs.

## Rules that matter

- Do not use `examples/` as live identity evidence.
- Do not guess missing owner identity fields.
- Do not ship generic claims like "powerful assistant" or "strong reasoning".
- Do not stop at placeholder-image state.
- Do not render the final card before the image-attached bundle passes validation.

## Good fit

OpenClaw ShrimpCard fits teams that want:

- agent showcase pages with stronger truthfulness guarantees
- a repeatable way to compress traces into public-facing copy
- a share-card format that stays compatible with strict schema checks
- a visual agent card that includes a real mascot asset instead of a mock placeholder

## Current demo inputs

The latest demo bundle in this repo was generated from live project evidence inside the current repository rather than `examples/`. The generated outputs were first written to `output/` and then the README-facing assets were copied into `docs/showcase/` for long-term retention.
