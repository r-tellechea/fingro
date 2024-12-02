import fingro

import numpy as np

def test_abelian():
	assert fingro.families.Cyclic(4).abelian
	assert not fingro.families.Dihedral(4).abelian

def test_element_orders():
	assert fingro.families.Cyclic(8).element_orders == (1,8,4,8,2,8,4,8)
	assert fingro.families.Dihedral(4).element_orders == (1,4,2,4,2,2,2,2)

def test_len():
	assert len(fingro.families.Cyclic(8)) == 8
	assert len(fingro.families.Dihedral(4)) == 8
