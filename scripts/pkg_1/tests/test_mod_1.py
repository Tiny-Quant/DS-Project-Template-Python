import sys 
sys.path.append("../../")
from pkg_1 import mod_1

def test_add():
    assert mod_1.add(2, 3) == 5