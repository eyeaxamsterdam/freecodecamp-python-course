# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '09-step-9.py')
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
    """You should have an else clause."""
    assert _Node(_code).find_ifs()[2].find_conditions()[1].is_empty()

def test_hint_2():
    """You should print User does not qualify for membership discount inside your else clause."""
    assert _Node(_code).find_ifs()[2].find_bodies()[1].has_call("print('User does not qualify for membership discount')")

def test_hint_3():
    """You should have print('Discount:', discount) below your if...else statement."""
    if_stmt = """if is_member:
        discount = 3
        print('User qualifies for membership discount')
    else:
        print('User does not qualify for membership discount')"""
    print_call = "print('Discount:', discount)"
    assert _Node(_code).is_ordered(if_stmt, print_call)
