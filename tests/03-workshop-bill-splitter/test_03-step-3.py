# Auto-generated from freeCodeCamp hints — do not edit
import sys, os, ast as _ast
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'helpers'))
from py_helpers import Node as _Node

_step = os.path.join(os.path.dirname(__file__), '..', '..', 'steps', '03-workshop-bill-splitter', '03-step-3.py')
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
    """You should define a variable named appetizers and assign it the value 37.89."""
    assert _Node(_code).find_variable('appetizers').is_equivalent('appetizers = 37.89')

def test_hint_2():
    """You should define a variable named main_courses and assign it the value 57.34."""
    assert _Node(_code).find_variable('main_courses').is_equivalent('main_courses = 57.34')

def test_hint_3():
    """You should define a variable named desserts and assign it the value 39.39."""
    assert _Node(_code).find_variable('desserts').is_equivalent('desserts = 39.39')

def test_hint_4():
    """You should define a variable named drinks and assign it the value 64.21."""
    assert _Node(_code).find_variable('drinks').is_equivalent('drinks = 64.21')
