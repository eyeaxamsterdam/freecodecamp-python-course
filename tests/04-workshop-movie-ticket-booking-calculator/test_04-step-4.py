# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '04-step-4.py')
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
    """You should have two if statements in your code."""
    assert _Node(_code).find_ifs()[1]

def test_hint_2():
    """Your second if statement condition should be age >= 21."""
    _cond = _Node(_code).find_ifs()[1].find_conditions()[0] 
    assert _cond.is_equivalent("age >= 21") or _cond.is_equivalent("21 <= age")

def test_hint_3():
    """You should print User is eligible for Evening shows inside your new if statement. Remember to surround the message with single or double quotes."""
    assert _Node(_code).find_ifs()[1].find_bodies()[0].has_call("print('User is eligible for Evening shows')")
