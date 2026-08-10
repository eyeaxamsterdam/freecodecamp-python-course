# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '01-workshop-report-card-printer', '07-step-7.py')
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
    """You should have an age variable."""
    assert _Node(_code).has_variable("age")

def test_hint_2():
    """The variable age should store the value 20. Do not surround the value with quotes."""
    assert _Node(_code).find_variable("age").is_equivalent("age = 20")

def test_hint_3():
    """You should print age and type(age) using a comma separator."""
    assert _Node(_code).has_call("print(age, type(age))")
