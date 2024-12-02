import fingro

def test_automorfisms_group():
	for p in [2,3,5,7]:
		Aut_Cp = fingro.compositions.AutomorphismsGroup(fingro.families.Cyclic(p))
		C_p_1 = fingro.families.Cyclic(p-1)
		assert Aut_Cp == C_p_1
