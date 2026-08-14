# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '02-step-2.py')
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
    """You should declare a variable named seat_type."""
    assert _Node(_code).has_variable("seat_type")

def test_hint_2():
    """You should assign the string Gold to seat_type. Remember to surround the value with either single or double quotes."""
    assert _Node(_code).find_variable("seat_type").is_equivalent("seat_type = 'Gold'")

def test_hint_3():
    """You should declare a variable named show_time."""
    assert _Node(_code).has_variable("show_time")

def test_hint_4():
    """You should assign the string Evening to show_time. Remember to surround the value with either single or double quotes."""
    assert _Node(_code).find_variable("show_time").is_equivalent("show_time = 'Evening'")
