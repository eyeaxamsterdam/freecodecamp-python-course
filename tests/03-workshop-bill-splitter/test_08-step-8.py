# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '03-workshop-bill-splitter', '08-step-8.py')
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
    """You should define a variable named each_pays."""
    assert _Node(_code).has_variable('each_pays')

def test_hint_2():
    """You should use the round() function to round final_bill to two decimal places and assign the result to your each_pays variable."""
    assert _Node(_code).find_variable('each_pays').is_equivalent('each_pays = round(final_bill, 2)')

def test_hint_3():
    """You should use print() to display the string Each person pays: followed by a space and your each_pays variable."""
    import io, contextlib, re

    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        exec(_code)

    match = re.search(r"Each person pays: ([0-9]+(?:\.[0-9]+)?)", buffer.getvalue())

    assert match
    assert abs(float(match.group(1)) - 62.13) < 1e-6
