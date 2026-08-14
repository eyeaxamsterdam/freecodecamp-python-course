# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '15-step-15.py')
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
    """You should have a fifth if statement."""
    assert _Node(_code).find_ifs()[4]

def test_hint_2():
    """Your fifth if statement condition should be age >= 21."""
    _cond = _Node(_code).find_ifs()[4].find_conditions()[0] 
    assert _cond.is_equivalent("age >= 21") or _cond.is_equivalent("21 <= age")

def test_hint_3():
    """You should print Ticket booking condition satisfied inside your new if statement. Remember to surround the message with single or double quotes."""
    assert _Node(_code).find_ifs()[4].find_bodies()[0].has_call("print('Ticket booking condition satisfied')")

def test_hint_4():
    """Your new if statement should have an else clause."""
    assert _Node(_code).find_ifs()[4].find_conditions()[1] == _Node()

def test_hint_5():
    """You should print Ticket booking failed due to restrictions inside your else clause. Remember to surround the message with single or double quotes."""
    assert _Node(_code).find_ifs()[4].find_bodies()[1].has_call("print('Ticket booking failed due to restrictions')")
