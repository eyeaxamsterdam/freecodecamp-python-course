# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '02-workshop-employee-profile-generator', '15-step-15.py')
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
    """You should have a variable named position."""
    assert _Node(_code).has_variable("position")

def test_hint_2():
    """You should assign the string Data Analyst to your position variable."""
    assert _Node(_code).find_variable("position").is_equivalent("position = 'Data Analyst'")

def test_hint_3():
    """You should have a variable named salary."""
    assert _Node(_code).has_variable("salary")

def test_hint_4():
    """You should assign the integer 75000 to your salary variable."""
    assert _Node(_code).find_variable("salary").is_equivalent("salary = 75000")

def test_hint_5():
    """You should update employee_card to use the f-string f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'."""
    assert _Node(_code).find_variable("employee_card").is_equivalent("employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'")

def test_hint_6():
    """You should print employee_card to the terminal."""
    assert _Node(_code).has_call("print(employee_card)")
