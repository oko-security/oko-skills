# /threat-model interview

Build the model in conversation with someone who owns or built the system,
using the four standard threat modeling questions. With `--seed <file>`, start
from an existing draft so the owner reviews and corrects instead of
describing everything from scratch.

For how to run the conversation (one question per turn, offer a likely answer,
check claims against the code), call the Skill tool with
`interviewing-system-owners`.

| # | Question | Feeds |
|---|---|---|
| 1 | What are we working on? | sections 1-3 |
| 2 | What can go wrong? | new section 4 rows: threat, actor, surface, asset |
| 3 | What are we going to do about it? | section 4 scoring, status, and controls; sections 5 and 8 |
| 4 | Did we do a good job? | ranking sanity check, coverage gaps, section 6 |

TODO(v0.2): a prompt bank for each question, seed-draft handling, and a
clear split in the output between facts confirmed in code and facts the owner
asserted.

Provenance: `mode: interview` (or `guided`), `owner: <name>`.
