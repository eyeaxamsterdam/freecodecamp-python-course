# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '02-workshop-employee-profile-generator', '02-step-2.py')
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
    """You should have a variable named full_name."""
    _Node(_code).has_variable("full_name")

def test_hint_2():
    """You should assign a string formed by concatenating first_name and last_name to your full_name variable."""
    _Node(_code).find_variable("full_name").is_equivalent("full_name = first_name + last_name")

def test_hint_3():
    """You should print the full_name variable."""
    _Node(_code).has_call("print(full_name)")
