#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const HELP_TEXT = `
Usage: node helpers/pullCourseStep.js <block> [step]
       node helpers/pullCourseStep.js next
       node helpers/pullCourseStep.js tests <block> [step]

Pulls a step (or every step) of a freeCodeCamp Python course workshop/lab
into its own file at steps/<block>/<NN>-<step-slug>.py. Also generates a
pytest test file at tests/<block>/test_<NN>-<step-slug>.py with the exact
same checks freeCodeCamp runs when you submit.

freeCodeCamp only records your real course progress when you submit
through their own website while logged in, there's no public submit API.
So the workflow is: solve locally, run pytest to check your work, then
paste the finished answer back into freeCodeCamp's editor to submit it.

Arguments:
  block        The block's dashed name, e.g. workshop-report-card-printer
               (this is the last segment of the URL when you're on that step)
  step         optional. A 1-based step number, e.g. 3. Omit to pull every step.
  next         Looks up the python-v9 course order and pulls every step of the
               first workshop/lab block you don't already have a steps/ folder
               for. Use this when you don't know (or don't want to look up) the
               next block's dashed name.
  tests        Regenerates only the test files for an already-pulled block,
               without touching your solution files.

Examples:
  node helpers/pullCourseStep.js workshop-report-card-printer
  node helpers/pullCourseStep.js workshop-report-card-printer 3
  node helpers/pullCourseStep.js next
  node helpers/pullCourseStep.js tests workshop-report-card-printer
`;

const blockUrl = (block) =>
  `https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/curriculum/structure/blocks/${block}.json`;
const stepMarkdownUrl = (block, id) =>
  `https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/curriculum/challenges/english/blocks/${block}/${id}.md`;
const superblockUrl =
  "https://raw.githubusercontent.com/freeCodeCamp/freeCodeCamp/main/curriculum/structure/superblocks/python-v9.json";

const stepLink = (block, stepDashedName) =>
  `https://www.freecodecamp.org/learn/python-v9/${block}/${stepDashedName}`;

function slugify(title) {
  return title
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function pad(n) {
  return String(n).padStart(2, "0");
}

function extractSection(md, marker) {
  const markers = ["# --description--", "# --hints--", "# --seed--", "## --seed-contents--"];
  const start = md.indexOf(marker);
  if (start === -1) return "";
  const afterStart = start + marker.length;
  let end = md.length;
  for (const m of markers) {
    if (m === marker) continue;
    const idx = md.indexOf(m, afterStart);
    if (idx !== -1 && idx < end) end = idx;
  }
  return md.slice(afterStart, end).trim();
}

function stripInlineCode(text) {
  return text.replace(/`([^`]*)`/g, "$1");
}

// Triple-backtick fenced blocks are pulled out and rendered as an indented
// snippet; single-backtick code spans are left alone (not stripped) since
// freeCodeCamp uses them to mark literal values, and stripping them can make
// a value like `, Apartment 4B` unreadable as plain prose.
function formatDescription(raw) {
  const fenceRegex = /```[a-zA-Z]*\n([\s\S]*?)```/g;
  const blocks = [];
  const withPlaceholders = raw.replace(fenceRegex, (_, code) => {
    const indented = code
      .trimEnd()
      .split("\n")
      .map((line) => `    ${line}`)
      .join("\n");
    blocks.push(indented);
    return `@@FENCE@${blocks.length - 1}@@`;
  });

  const stripped = withPlaceholders
    .split("\n")
    .map((line) => line.replace(/^\s*-\s+/, ""))
    .join("\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();

  return stripped.replace(/@@FENCE@(\d+)@@/g, (_, i) => blocks[Number(i)]);
}

function extractSeedCode(md) {
  const section = extractSection(md, "## --seed-contents--");
  const match = section.match(/```[a-zA-Z]*\n([\s\S]*?)```/);
  return match ? match[1].trim() : "";
}

// The literal `--fcc-editable-region--` marker text is only meaningful
// inside freeCodeCamp's own editor and isn't valid Python on its own, so
// it's commented out here to keep the generated file syntactically valid.
function commentOutEditableRegionMarkers(seedCode) {
  return seedCode
    .split("\n")
    .map((line) => (line.trim() === "--fcc-editable-region--" ? "# --fcc-editable-region--" : line))
    .join("\n");
}

function buildPythonHeader({ title, description, link }) {
  return `"""\n${title}\n${description}\n\nLink: ${link}\n"""`;
}

// Parse the # --hints-- section and pull out Python assertions from
// runPython(`...`) calls. Each hint becomes { description, assertion }.
function extractPythonHints(md) {
  const hintsSection = extractSection(md, "# --hints--");
  if (!hintsSection) return [];

  const hints = [];
  const parts = hintsSection.split("```js\n");
  for (let i = 1; i < parts.length; i++) {
    const descLines = parts[i - 1].trim().split("\n").filter((l) => l.trim());
    const description = stripInlineCode(descLines[descLines.length - 1] || "");
    const jsBlock = parts[i].split("```")[0];
    // Pattern A: assert(runPython(`expr`)) — JS-level assertion, Python is a bare expression
    const assertWrap = jsBlock.match(/assert\(runPython\(`([\s\S]*?)`\)\)/);
    if (assertWrap) {
      hints.push({ description, assertion: `assert ${assertWrap[1].trim().replace(/\\\$/g, '$').replace(/\\\\\./g, '\\.')}` });
      continue;
    }
    // Pattern B: runPython(`assert ...`) — Python-level assertion already in the code
    const pythonMatch = jsBlock.match(/runPython\(`([\s\S]*?)`\)/);
    if (pythonMatch) {
      hints.push({ description, assertion: pythonMatch[1].replace(/\\\$/g, '$').replace(/\\\\\./g, '\\.') });
    }
  }
  return hints;
}

// Build a pytest file that runs freeCodeCamp's exact checks against the step file.
// _code is set to the step file content with the instructions docstring stripped,
// matching what freeCodeCamp passes to its test runner as the student's code.
function buildTestFile(blockDir, stepFileName, hints) {
  if (hints.length === 0) return null;

  const lines = [
    "# Auto-generated from freeCodeCamp hints — do not edit",
    "import sys, os, ast as _ast",
    "sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))",
    "from py_helpers import Node as _Node",
    "",
    `_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '${blockDir}', '${stepFileName}')`,
    "with open(_step) as _f:",
    "    _raw = _f.read()",
    "# strip the instructions docstring added by pullCourseStep.js",
    "_tree = _ast.parse(_raw)",
    "if _tree.body and isinstance(_tree.body[0], _ast.Expr) and isinstance(_tree.body[0].value, _ast.Constant):",
    "    _end = _tree.body[0].end_lineno",
    "    _code = '\\n'.join(_raw.splitlines()[_end:]).strip()",
    "else:",
    "    _code = _raw",
    "",
  ];

  for (let i = 0; i < hints.length; i++) {
    const { description, assertion } = hints[i];
    lines.push(`def test_hint_${i + 1}():`);
    if (description) lines.push(`    """${description}"""`);
    const assertionLines = assertion.split("\n");
    const nonEmpty = assertionLines.filter((l) => l.trim());
    const minIndent = nonEmpty.length
      ? Math.min(...nonEmpty.map((l) => l.match(/^(\s*)/)[1].length))
      : 0;
    const dedented = assertionLines.map((l) => (l.trim() ? l.slice(minIndent) : ""));
    // drop leading/trailing blank lines produced by the backtick delimiters
    while (dedented.length && !dedented[0].trim()) dedented.shift();
    while (dedented.length && !dedented[dedented.length - 1].trim()) dedented.pop();
    // freeCodeCamp writes hints two ways: some embed `assert` inside the
    // runPython(`...`) string, others wrap the whole runPython(...) call in
    // a JS-level assert(...) and leave the Python string as a bare
    // expression. Normalize to the former so a false result actually fails
    // the pytest test instead of silently being evaluated and discarded.
    // Only add assert if the block has no assert anywhere — multi-line hints
    // that start with `import` or assignments already contain their own asserts.
    const hasAssert = dedented.some((l) => /^assert\b/.test(l.trim()));
    if (!hasAssert) {
      const firstNonBlank = dedented.findIndex((l) => l.trim());
      if (firstNonBlank !== -1) {
        dedented[firstNonBlank] = `assert ${dedented[firstNonBlank]}`;
      }
    }
    // Lines inside an already-open triple-quoted string (e.g. an embedded
    // `if_stmt = """...\n..."""` snippet used with is_ordered) are literal
    // string content, not statements — indenting them would shift their
    // characters and desync the embedded code's own indentation, breaking
    // it when that string is later parsed as Python on its own. Only add
    // the function-body indent to lines that are actual statements.
    let inTripleQuoted = false;
    for (const line of dedented) {
      const shouldIndent = !inTripleQuoted;
      if (((line.match(/"""/g) || []).length) % 2 === 1) inTripleQuoted = !inTripleQuoted;
      lines.push(line.trim() ? (shouldIndent ? `    ${line}` : line) : "");
    }
    lines.push("");
  }

  return lines.join("\n");
}

async function fetchBlock(block) {
  const res = await fetch(blockUrl(block));
  if (!res.ok) throw new Error(`No block named "${block}" (HTTP ${res.status})`);
  return res.json();
}

// Only workshop/lab blocks have step-by-step editable code; lecture, review,
// quiz, and exam blocks are just reading/video content with nothing to pull.
async function fetchOrderedPullableBlocks() {
  const res = await fetch(superblockUrl);
  if (!res.ok) throw new Error(`Couldn't fetch the course structure (HTTP ${res.status})`);
  const data = await res.json();
  const blocks = [];
  for (const chapter of data.chapters) {
    for (const module of chapter.modules) {
      for (const block of module.blocks) {
        if (block.startsWith("workshop-") || block.startsWith("lab-")) blocks.push(block);
      }
    }
  }
  return blocks;
}

// Folders on disk are prefixed with their course-order number (see
// blockDirName below) so they sort correctly in a file browser; strip that
// back off to compare against the raw dashed names from the course structure.
function alreadyPulledBlocks(stepsDir) {
  if (!fs.existsSync(stepsDir)) return new Set();
  return new Set(
    fs
      .readdirSync(stepsDir, { withFileTypes: true })
      .filter((e) => e.isDirectory())
      .map((e) => e.name.replace(/^\d+-/, ""))
  );
}

function blockDirName(block, orderedBlocks) {
  const index = orderedBlocks.indexOf(block);
  return index === -1 ? block : `${pad(index + 1)}-${block}`;
}

async function fetchStepMarkdown(block, id) {
  const res = await fetch(stepMarkdownUrl(block, id));
  if (!res.ok) throw new Error(`Couldn't fetch step ${id} (HTTP ${res.status})`);
  return res.text();
}

async function pullStep(block, dirName, index, entry, blockDir, testsOnly = false) {
  const md = await fetchStepMarkdown(block, entry.id);
  const stepDashedName = `step-${index}`;
  const fileName = `${pad(index)}-${slugify(entry.title)}.py`;

  if (!testsOnly) {
    const description = formatDescription(extractSection(md, "# --description--"));
    const seedCode = commentOutEditableRegionMarkers(extractSeedCode(md));
    const header = buildPythonHeader({
      title: entry.title,
      description,
      link: stepLink(block, stepDashedName),
    });
    const content = `${header}\n\n${seedCode}\n`;
    fs.writeFileSync(path.join(blockDir, fileName), content, "utf8");
    console.log(`✅  Created steps/${dirName}/${fileName}`);
  }

  const hints = extractPythonHints(md);
  if (hints.length > 0) {
    const testDir = path.join(__dirname, "..", "tests", dirName);
    fs.mkdirSync(testDir, { recursive: true });
    const testContent = buildTestFile(dirName, fileName, hints);
    fs.writeFileSync(path.join(testDir, `test_${fileName}`), testContent, "utf8");
    console.log(`🧪  Created tests/${dirName}/test_${fileName}`);
  }
}

async function pullBlock(block, stepArg, orderedBlocks, testsOnly = false) {
  let data;
  try {
    data = await fetchBlock(block);
  } catch (err) {
    console.error(`⚠️  ${err.message}`);
    process.exitCode = 1;
    return;
  }

  const steps = data.challengeOrder;
  const dirName = blockDirName(block, orderedBlocks);
  const blockDir = path.join(__dirname, "..", "steps", dirName);
  if (!testsOnly) fs.mkdirSync(blockDir, { recursive: true });

  if (stepArg) {
    const index = Number(stepArg);
    const entry = steps[index - 1];
    if (!entry) {
      console.error(`⚠️  "${block}" only has ${steps.length} steps, there's no step ${stepArg}.`);
      process.exitCode = 1;
      return;
    }
    await pullStep(block, dirName, index, entry, blockDir, testsOnly);
    return;
  }

  for (let i = 0; i < steps.length; i++) {
    await pullStep(block, dirName, i + 1, steps[i], blockDir, testsOnly);
  }
}

async function pullNextBlock(orderedBlocks) {
  const stepsDir = path.join(__dirname, "..", "steps");
  const pulled = alreadyPulledBlocks(stepsDir);

  const next = orderedBlocks.find((block) => !pulled.has(block));
  if (!next) {
    console.log("🎉  Every workshop/lab block in python-v9 already has a steps/ folder.");
    return;
  }

  console.log(`▶️  Next block: ${next}`);
  await pullBlock(next, undefined, orderedBlocks);
}

async function main() {
  const argv = process.argv.slice(2);

  if (argv.length === 0 || argv.includes("-h") || argv.includes("--help")) {
    console.log(HELP_TEXT);
    return;
  }

  let orderedBlocks;
  try {
    orderedBlocks = await fetchOrderedPullableBlocks();
  } catch (err) {
    console.error(`⚠️  ${err.message}`);
    process.exitCode = 1;
    return;
  }

  if (argv[0] === "next") {
    await pullNextBlock(orderedBlocks);
    return;
  }

  if (argv[0] === "tests") {
    const [, block, stepArg] = argv;
    if (!block) {
      console.error("⚠️  Provide a block name: node helpers/pullCourseStep.js tests <block>");
      process.exitCode = 1;
      return;
    }
    await pullBlock(block, stepArg, orderedBlocks, true);
    return;
  }

  const [block, stepArg] = argv;
  await pullBlock(block, stepArg, orderedBlocks);
}

main();
