# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '13-step-13.py')
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
    assert _Node(_code).find_ifs()[3].find_conditions()[1].is_empty()

def test_hint_2():
    """You should print No extra charges will be applied inside your else clause. Remember to surround the message with single or double quotes."""
    assert _Node(_code).find_ifs()[3].find_bodies()[1].has_call("print('No extra charges will be applied')")

def test_hint_3():
    """You should have print('Extra charges:', extra_charges) below your if...else statement."""
    if_stmt = """if is_weekend:
        extra_charges = 2
        print('Extra charges will be applied')
    else:
        print('No extra charges will be applied')"""
    print_call = "print('Extra charges:', extra_charges)"
    assert _Node(_code).is_ordered(if_stmt, print_call)
