# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '06-step-6.py')
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
    """You should declare a variable named is_member."""
    assert _Node(_code).has_variable("is_member")

def test_hint_2():
    """You should assign the boolean value True to is_member. Do not surround the value with quotes."""
    assert _Node(_code).find_variable("is_member").is_equivalent("is_member = True")

def test_hint_3():
    """You should declare a variable named is_weekend."""
    assert _Node(_code).has_variable("is_weekend")

def test_hint_4():
    """You should assign the boolean value False to is_weekend. Do not surround the value with quotes."""
    assert _Node(_code).find_variable("is_weekend").is_equivalent("is_weekend = False")
