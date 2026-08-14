# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '20-step-20.py')
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
    """You should have an elif clause."""
    _cond = _Node(_code).find_ifs()[4].find_ifs()[0].find_conditions()[1]
    assert not _cond.is_empty()

def test_hint_2():
    """Your elif clause condition should be seat_type == 'Gold'."""
    _cond = _Node(_code).find_ifs()[4].find_ifs()[0].find_conditions()[1] 
    assert _cond.is_equivalent("seat_type == 'Gold'")

def test_hint_3():
    """You should assign the integer value 3 to service_charges variable inside your elif body."""
    _var = _Node(_code).find_ifs()[4].find_ifs()[0].find_bodies()[1].find_variable("service_charges") 
    assert _var.is_equivalent("service_charges = 3")

def test_hint_4():
    """You should have print('Service charges:', service_charges) below your if...elif...else statement."""
    if_stmt = """if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1"""
    print_call = "print('Service charges:', service_charges)"
    assert _Node(_code).find_ifs()[4].find_bodies()[0].is_ordered(if_stmt, print_call)
