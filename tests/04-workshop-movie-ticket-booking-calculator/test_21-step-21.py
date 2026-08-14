# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '04-workshop-movie-ticket-booking-calculator', '21-step-21.py')
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
    """You should declare a variable named final_price."""
    assert _Node(_code).find_ifs()[4].find_bodies()[0].has_variable("final_price")

def test_hint_2():
    """You should assign the value base_price + extra_charges + service_charges - discount to final_price."""
    import itertools  
    perms = itertools.permutations(['+ base_price', '+ extra_charges', '+ service_charges', '- discount'])  
    values = (' '.join(perm).lstrip('+') for perm in perms)  
    solutions = (f'final_price = {v}' for v in values)  
    var = _Node(_code).find_ifs()[4].find_bodies()[0].find_variable("final_price")  
    assert any(var.is_equivalent(s) for s in solutions)

def test_hint_3():
    """You should have print('Final price of ticket:', final_price) below your final_price variable."""
    print_call = "print('Final price of ticket:', final_price)"  
    _body = _Node(_code).find_ifs()[4].find_bodies()[0]
    assert _body.has_call(print_call)
