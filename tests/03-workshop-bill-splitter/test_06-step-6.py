# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '03-workshop-bill-splitter', '06-step-6.py')
with open(_step) as _f:
    _raw = _f.read()
# strip the instructions docstring added by pullCourseStep.js
_tree = _ast.parse(_raw)
if _tree.body and isinstance(_tree.body[0], _ast.Expr) and isinstance(_tree.body[0].value, _ast.Constant):
    _end = _tree.body[0].end_lineno
    _code = '\n'.join(_raw.splitlines()[_end:]).strip()
else:
    _code = _raw

def test_hint_1():
    """You should use the += operator to add the value of tip to your running_total."""
    assert _Node(_code).has_stmt('running_total += tip')

def test_hint_2():
    """You should print the string Total with tip: followed by a space and the running_total variable."""
    import io, contextlib, re

    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        exec(_code)

    match = re.search(r"Total with tip: ([0-9]+(?:\.[0-9]+)?)", buffer.getvalue())

    assert match
    assert abs(float(match.group(1)) - ((37.89 + 57.34 + 39.39 + 64.21) * 1.25)) < 1e-6
