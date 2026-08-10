# freeCodeCamp Python Course

A local copy of freeCodeCamp's Python course workshop/lab steps, pulled one
step at a time so they can be solved in a real editor instead of freeCodeCamp's
in-browser one.

freeCodeCamp only records progress when you submit through their own site
while logged in — there's no public submit API. So the workflow is:

1. Pull a step (or a whole workshop/lab) with the script below.
2. Solve it locally, with your own shortcuts, linting, etc.
3. Paste the finished code back into freeCodeCamp's editor to actually submit it.

## Usage

```bash
node helpers/pullCourseStep.js next              # pull the next workshop/lab you haven't started
node helpers/pullCourseStep.js <block>            # pull every step of a known block
node helpers/pullCourseStep.js <block> <step>     # pull just one step
```

`<block>` is the dashed name from the URL, e.g. `workshop-report-card-printer`.

`next` looks up freeCodeCamp's own course structure and pulls the first
workshop/lab block that doesn't already have a `steps/` folder — lectures,
reviews, and quizzes are skipped since there's no code to pull for those.

## Structure

Each pulled step becomes its own file:

```
steps/<NN>-<block>/<NN>-<step-slug>.py
```

The number prefixes are course order, so folders and files sort correctly
in a file browser. Every file has a docstring with the step's instructions
and a link back to the real freeCodeCamp page, followed by the starter code.

## Notes

- Personal practice copy only — no tests, hints, or answers are pulled, just
  the description and starter code.
- Not affiliated with freeCodeCamp; just reads their public curriculum data
  from GitHub.
