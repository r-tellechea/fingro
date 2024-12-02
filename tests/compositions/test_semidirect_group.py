import fingro

def test_semidirect_group():
	C2 = fingro.families.Cyclic(2)
	C7 = fingro.families.Cyclic(7)
	D7 = fingro.families.Dihedral(7)

	f0, f1 = tuple(
		fingro
		.compositions
		.compose_functions
		.get_homomorphisms(
			C2,
			fingro.compositions.AutomorphismsGroup(C7)
		)
	)

	assert C2 * C7 == fingro.compositions.SemidirectProduct(C2, C7, f0, check_homomorphism=False)
	assert D7 == fingro.compositions.SemidirectProduct(C2, C7, f1, check_homomorphism=False)
