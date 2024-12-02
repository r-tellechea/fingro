import fingro

def test_isomorphism_group():
	D2 = fingro.families.Dihedral(2)
	D3 = fingro.families.Dihedral(3)
	C2 = fingro.families.Cyclic(2)
	C2xC2 = C2 * C2
	Iso_C2C2_D2 = fingro.compositions.IsomorphismsGroup(C2xC2, D2)

	assert Iso_C2C2_D2 == D3
