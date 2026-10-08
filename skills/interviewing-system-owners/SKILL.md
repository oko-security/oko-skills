---
name: interviewing-system-owners
description: Use when a system owner, architect, or engineer is available to answer questions for a threat model or security design review. Works through the four standard threat modeling questions one at a time, proposes a likely answer for each, and checks claims against the code.
---

# Interviewing system owners

The owner's time is the scarcest input you have. Ask only what the code
can't answer.

## How to ask

- **One question per turn.** Wait for the reply before you ask anything else.
- **Propose an answer first.** Base it on the code or the draft: "In
  `api/auth.py:40` every route requires a session except `/health` and
  `/webhook`. Is that right?" Confirming or correcting is much quicker than
  answering from scratch.
- **Check what you hear.** After each answer, look in the code. Label each
  fact `verified` (with a `file:line`) or `owner-stated`. Owner-stated facts
  that matter go in section 6.
- **Move on when the answers dry up.** If several answers in a row add
  nothing new, go to the next question.

## The four questions

1. **What are we working on?** Confirm the purpose, users, deployment, data,
   assets, and entry points. Ask about anything the repository can't show:
   admin consoles, scheduled jobs, partner integrations, support tools.
2. **What can go wrong?** Start by asking what worries them most. Then go
   through the top entry points with STRIDE (call the Skill tool with
   `applying-threat-lenses`) and ask about the categories they haven't
   mentioned.
3. **What are we going to do about it?** Cover controls already in place in
   code, infrastructure, and process, along with risks they accept and work
   they have planned.
4. **Did we do a good job?** Read out the top five threats and ask what is
   missing or in the wrong order.

## Starting from a draft

Use the draft's section 6 questions as your opening questions. Edit rows in
place as the owner confirms or corrects them, and keep the existing IDs.

TODO(v0.2): a prompt bank for each question, and a standard way to handle "I
don't know" (record it in section 6 with a suggested person to ask).
