import fingro

def test_endomorphism_group():
	C8 = fingro.families.Cyclic(8)
	End_C8_C8 = fingro.compositions.EndomorphismsGroup(C8)
	assert End_C8_C8 == C8
