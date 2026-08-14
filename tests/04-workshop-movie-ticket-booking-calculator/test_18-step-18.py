# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '18-step-18.py')
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
    """You should declare a variable named service_charges inside your last if statement body."""
    assert _Node(_code).find_ifs()[4].find_bodies()[0].has_variable("service_charges")

def test_hint_2():
    """You should assign the integer value 0 to service_charges."""
    _var = _Node(_code).find_ifs()[4].find_bodies()[0].find_variable("service_charges") 
    assert _var.is_equivalent("service_charges = 0")

def test_hint_3():
    """You should have an if statement inside your last if statement body."""
    assert _Node(_code).find_ifs()[4].find_ifs()[0]

def test_hint_4():
    """The new if statement condition should be seat_type == 'Premium'."""
    _cond = _Node(_code).find_ifs()[4].find_ifs()[0].find_conditions()[0] 
    assert _cond.is_equivalent("seat_type == 'Premium'")

def test_hint_5():
    """You should assign the integer value 5 to service_charges variable inside your new if statement."""
    _var = _Node(_code).find_ifs()[4].find_ifs()[0].find_bodies()[0].find_variable("service_charges") 
    assert _var.is_equivalent("service_charges = 5")
