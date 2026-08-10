# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '02-workshop-employee-profile-generator', '12-step-12.py')
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
    """You should have a variable named experience_years."""
    _Node(_code).has_variable("experience_years")

def test_hint_2():
    """You should assign the integer 5 to your experience_years variable."""
    _Node(_code).find_variable("experience_years").is_equivalent("experience_years = 5")

def test_hint_3():
    """You should have a variable named experience_info."""
    _Node(_code).has_variable("experience_info")

def test_hint_4():
    """You should assign a string formed by concatenating 'Experience: ', str(experience_years), and ' years' to your experience_info variable."""
    _Node(_code).find_variable("experience_info").is_equivalent("experience_info = 'Experience: ' + str(experience_years) + ' years'")

def test_hint_5():
    """You should print experience_info."""
    _Node(_code).has_call("print(experience_info)")
