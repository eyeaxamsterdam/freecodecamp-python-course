# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '02-workshop-employee-profile-generator', '01-step-1.py')
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
    """You should have a variable named first_name."""
    assert _Node(_code).has_variable("first_name")

def test_hint_2():
    """You should assign the string John to your first_name variable. Remember to enclose the text between either single or double quotes."""
    assert _Node(_code).find_variable("first_name").is_equivalent("first_name = 'John'")

def test_hint_3():
    """You should assign the string Doe to your last_name variable. Remember to enclose the text between either single or double quotes."""
    assert _Node(_code).find_variable("last_name").is_equivalent("last_name = 'Doe'")

def test_hint_4():
    """You should print your first_name variable to the terminal."""
    assert _Node(_code).has_call("print(first_name)")

def test_hint_5():
    """You should print your last_name variable to the terminal."""
    assert _Node(_code).has_call("print(last_name)")
