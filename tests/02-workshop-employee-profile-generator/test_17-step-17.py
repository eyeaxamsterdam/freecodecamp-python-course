# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '02-workshop-employee-profile-generator', '17-step-17.py')
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
    """You should have a variable named year_code."""
    assert _Node(_code).has_variable("year_code")

def test_hint_2():
    """You should slice employee_code from index 4 to 8 and assign the result to your year_code variable."""
    assert _Node(_code).find_variable("year_code").is_equivalent("year_code = employee_code[4:8]")

def test_hint_3():
    """You should have a variable named initials."""
    assert _Node(_code).has_variable("initials")

def test_hint_4():
    """You should slice employee_code from index 9 to 11 and assign the result to your initials variable."""
    assert _Node(_code).find_variable("initials").is_equivalent("initials = employee_code[9:11]")

def test_hint_5():
    """You should print year_code to the terminal."""
    assert _Node(_code).has_call("print(year_code)")

def test_hint_6():
    """You should print initials to the terminal."""
    assert _Node(_code).has_call("print(initials)")
