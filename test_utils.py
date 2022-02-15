import pytest
import utils
import math

def test_fact():
    assert utils.fact(4) == 24

def test_roots():
    assert utils.roots(1,1,-1) == (0.6180339887498949, -2.118033988749895)

def test_integrate():
    assert math.isclose(utils.integrate('x ** 2 - 1',-1,1), -4/3 , rel_tol = 1e-2) #isclose compare les deux resultats 


