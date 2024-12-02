import fingro

def test_eq():
	C2 = fingro.families.Cyclic(2)
	C3 = fingro.families.Cyclic(3)
	D2 = fingro.families.Dihedral(2)
	D4 = fingro.families.Dihedral(4)
	assert C3 == C3
	assert D4 == D4
	assert C2 * C2 == D2

def test_ne():
	C8 = fingro.families.Cyclic(8)
	D4 = fingro.families.Dihedral(4)
	assert C8 != D4

def test_lt():
	C2 = fingro.families.Cyclic(2)
	C3 = fingro.families.Cyclic(3)
	C4 = fingro.families.Cyclic(4)
	assert C2 < C4
	assert not C2 < C3
	assert not C3 < C4
