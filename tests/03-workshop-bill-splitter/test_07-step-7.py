# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '03-workshop-bill-splitter', '07-step-7.py')
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
    """You should define a variable named final_bill."""
    assert _Node(_code).has_variable('final_bill')

def test_hint_2():
    """You should use the / operator to divide running_total by num_of_friends and assign the result to your final_bill variable."""
    assert _Node(_code).find_variable('final_bill').is_equivalent('final_bill = running_total / num_of_friends')

def test_hint_3():
    """You should print the string Bill per person: followed by a space and the final_bill variable."""
    import io, contextlib, re

    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        exec(_code)

    match = re.search(r"Bill per person: ([0-9]+(?:\.[0-9]+)?)", buffer.getvalue())

    assert match
    assert abs(float(match.group(1)) - (((37.89 + 57.34 + 39.39 + 64.21) * 1.25) / 4)) < 1e-6
