---
name: openclaw-shrimpcard
description: Create ShrimpCard outputs for OpenClaw. Use when users ask to generate a lobster/shrimp card, or need accurate JSON/image outputs matching the ShrimpCard schema for sharing or rendering.
---

# OpenClaw ShrimpCard

## Overview
Generate accurate ShrimpCard JSON (and optional image/description) from user input and memory, then validate the result against the schema before output.

## Workflow

1. Gather required fields
- Required: `name`, `tagline`, `description`, `top_skills` (3), `owner.name`, `lobster_image_desc`, `card_id`.
- If any required info is missing, ask the user for it.

2. Build the card object
- Follow `references/card-schema.json`.
- Ensure `lobster_image_desc` is a lobster/shrimp image description.
- If an image is not available, set `image.placeholder` and keep `lobster_image_desc`.

3. Validate before output
- Run `scripts/validate_card.py <json-file>`.
- If validation fails, fix the data and re-validate.

4. Output
- If the user wants a file, write `shrimp-card.json` to disk.
- Provide a JSON file and paste the JSON in the response.
- If the user requests an image, either include an image URL/data_url or provide the image description for rendering.

5. Image prompt assistance (optional)
- If the user wants to self-generate an image, provide the prompt template from `references/card-spec.md`.
- Remind them to capture and composite the QR into the footer square if a QR is provided.

## Accuracy Rules
- Do not invent owner details or contacts. Ask if missing.
- Keep `top_skills` to exactly 3 items. They are capability tags chosen by OpenClaw (not necessarily most-used skills).
- Keep text concise enough to fit the card layout.

## Resources

### scripts/
- `validate_card.py`: Validate JSON against required fields and constraints.

### references/
- `card-schema.json`: JSON schema.
- `sample-card.json`: Example payload.
- `card-spec.md`: Field requirements and style notes.
