# Code Review: Stages 1–3

## Summary

| | |
|---|---|
| **Files reviewed** | 7 |
| **Files changed** | 4 |
| **Clean files** | 3 |
| **Problems fixed** | 22, plus 4 typos in a later cleanup |
| **Small items left unfixed** | 9 |

All 5 tutorial and RawCode stage files still compile. I checked the Stage 3 and Stage 1 RawCode changes in the diff, but not the comment edits in the Stage 1 and Stage 2 tutorials.

> **Before you trust the Stage 3 fixes:** play one real game. pygame isn't installed here, so the agent tested the logic against a small pygame stand-in with a bot player. Rendering, keyboard input and the window are untested.

## Fixes by stage

### Stage 3

File: [LearnPythonStage3.py](Learn%20Python%20Here!/Stage%203/LearnPythonStage3.py)

| Problem | What was wrong | Result |
|---|---|---|
| **Frozen ball** (worst bug) | After a hit near the paddle's edge, sideways speed could drop to 0.1, which `int()` rounds to 0. The ball then bounced up and down forever and nobody could score. | Happened in all 40 simulated games before the fix and none after. |
| **Ball passing through paddles** | The speed limit of 250 let the ball jump a paddle in one frame. | The limit is now 21. |
| **`serving_to_player`** | It meant the opposite of its name. | Fixed. Whoever loses the point still receives the serve. |

### Stage 1

**[LearnPythonStage1.py](Learn%20Python%20Here!/Stage%201/LearnPythonStage1.py): 14 fixes, mostly wrong teaching comments**

Examples of what was wrong:

- `range()` and `self` were called keywords.
- `range` was said to always start at 0.
- One output comment showed `True` in a set that drops it.
- `my_function` was decorated but never called, so the decorator demo printed nothing. It's called now.

**[LearnPythonStage1RawCode.py](Learn%20Python%20Here!/Stage%201/LearnPythonStage1RawCode.py)**

- It had `import requests` and a live web request that the tutorial doesn't have, and it crashed at the end without that package.
- Both are removed, and the file now matches the tutorial.

### Stage 2

**[LearnPythonStage2.py](Learn%20Python%20Here!/Stage%202/LearnPythonStage2.py): 4 comment fixes**

- It said list methods handle removing a missing element, but `remove` raises an error.
- It implied Python has function overloads.
- Two references said "lesson 1" instead of Stage 1, and one of those also wrongly claimed Stage 1 had covered list methods.

### Clean files

- `TEST #1.py`
- `my_module.py`
- `LearnPythonStage2RawCode.py`

## Other things to know

- **Commit message:** the agent found no pygame code in Stage 2; it's in Stage 3. The commit message on `a6e328d` says otherwise.
- **Left unfixed:** 9 small items, including the unused `dt` and `import os`, and Lesson 7 being titled "Dictionary Methods" without showing any. The agent's report listed 11, and the 2 typo items among them have since been fixed.

## Your decisions

All four changes are applied, and I'd keep them all.

| # | Change | Why keep it | Downside or alternative |
|---|---|---|---|
| 1 | **`requests` removal** | The tutorial never taught it. | If it was a deliberate bonus, restore it from git and add it to the tutorial with an install note. |
| 2 | **Speed limit of 21** | The alternative is collision code that's harder for beginners to read. | It changes how fast rallies feel. |
| 3 | **Serve direction** | The loser of each point keeps receiving the serve, as before. | None. |
| 4 | **`my_function()` call** | It's worth it for a working demo. | It adds one second and one output line to both Stage 1 files. |
