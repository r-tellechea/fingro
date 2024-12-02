import fingro

def test_is_subgroup():
	C3 = fingro.families.Cyclic(3)
	C4 = fingro.families.Cyclic(4)
	C6 = fingro.families.Cyclic(6)
	D4 = fingro.families.Dihedral(4)

	assert fingro.fn.is_subgroup(C3, C3)
	assert fingro.fn.is_subgroup(C4, C4)
	assert fingro.fn.is_subgroup(C6, C6)
	assert fingro.fn.is_subgroup(D4, D4)

	assert fingro.fn.is_subgroup(C3, C6)
	assert fingro.fn.is_subgroup(C4, D4)

	assert not fingro.fn.is_subgroup(C3, C4)
	assert not fingro.fn.is_subgroup(C3, D4)
	assert not fingro.fn.is_subgroup(C6, D4)
