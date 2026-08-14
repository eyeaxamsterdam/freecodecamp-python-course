# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '01-step-1.py')
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
    """You should declare a variable named base_price."""
    assert _Node(_code).has_variable("base_price")

def test_hint_2():
    """You should assign the integer value 15 to base_price."""
    assert _Node(_code).find_variable("base_price").is_equivalent("base_price = 15")

def test_hint_3():
    """You should declare a variable named age."""
    assert _Node(_code).has_variable("age")

def test_hint_4():
    """You should assign the integer value 21 to age."""
    assert _Node(_code).find_variable("age").is_equivalent("age = 21")
