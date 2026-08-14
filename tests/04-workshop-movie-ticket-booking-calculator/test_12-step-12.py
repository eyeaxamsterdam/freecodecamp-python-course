# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '12-step-12.py')
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
    """You should declare a variable named extra_charges."""
    assert _Node(_code).has_variable("extra_charges")

def test_hint_2():
    """You should assign the integer value 0 to extra_charges."""
    assert _Node(_code).find_variable("extra_charges").is_equivalent("extra_charges = 0")

def test_hint_3():
    """You should have a fourth if statement."""
    assert _Node(_code).find_ifs()[3]

def test_hint_4():
    """Your fourth if statement condition should be is_weekend."""
    assert _Node(_code).find_ifs()[3].find_conditions()[0].is_equivalent("is_weekend")

def test_hint_5():
    """You should assign the integer value 2 to extra_charges variable inside your new if statement."""
    _var = _Node(_code).find_ifs()[3].find_bodies()[0].find_variable("extra_charges") 
    assert _var.is_equivalent("extra_charges = 2")

def test_hint_6():
    """You should print Extra charges will be applied inside your new if statement. Remember to surround the message with single or double quotes."""
    assert _Node(_code).find_ifs()[3].find_bodies()[0].has_call("print('Extra charges will be applied')")
