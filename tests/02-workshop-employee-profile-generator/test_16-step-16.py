# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '02-workshop-employee-profile-generator', '16-step-16.py')
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
    """You should have a variable named employee_code."""
    _Node(_code).has_variable("employee_code")

def test_hint_2():
    """You should assign the string DEV-2026-JD-001 to your employee_code variable."""
    _Node(_code).find_variable("employee_code").is_equivalent("employee_code = 'DEV-2026-JD-001'")

def test_hint_3():
    """You should have a variable named department."""
    _Node(_code).has_variable("department")

def test_hint_4():
    """You should slice the first three characters of employee_code and assign them to your department variable."""
    dep = _Node(_code).find_variable("department")
    assert dep.is_equivalent("department = employee_code[0:3]") or dep.is_equivalent("department = employee_code[:3]")

def test_hint_5():
    """You should print department to the terminal."""
    _Node(_code).has_call("print(department)")
