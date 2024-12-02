import fingro

def test_homomorphism_group():
	C8 = fingro.families.Cyclic(8)
	Hom_C8_C8 = fingro.compositions.HomomorphismsGroup(C8, C8)
	assert Hom_C8_C8 == C8
