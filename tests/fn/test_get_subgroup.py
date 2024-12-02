import fingro
import numpy as np

def test_get_subgroup():
	C4 = fingro.families.Cyclic(4)
	D4 = fingro.families.Dihedral(4)
	H = fingro.fn.get_subgroup(C4, D4)
	assert fingro.same_matrix(H.group, D4)
	assert C4 == H
