import fingro

def test_center():
	C8 = fingro.families.Cyclic(8)
	D4 = fingro.families.Dihedral(4)
	assert fingro.fn.center(C8) == C8
	assert fingro.fn.center(D4) == fingro.families.Cyclic(2)
