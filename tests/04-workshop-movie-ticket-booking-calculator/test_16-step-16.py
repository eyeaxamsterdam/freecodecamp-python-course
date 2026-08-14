# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '16-step-16.py')
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
    """Your last if statment condition should be age >= 21 or age >= 18 and show_time != 'Evening'."""
    _cond = _Node(_code).find_ifs()[4].find_conditions()[0] 
    _first = _cond.is_equivalent("age >= 21 or age >= 18 and show_time != 'Evening'")
    _second = _cond.is_equivalent("age >= 21 or 18 <= age and show_time != 'Evening'")
    assert _first or _second
