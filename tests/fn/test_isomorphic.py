import fingro

def test_isomorphic():
	C3 = fingro.families.Cyclic(3)
	C4 = fingro.families.Cyclic(4)
	C6 = fingro.families.Cyclic(6)
	D4 = fingro.families.Dihedral(4)
	D17 = fingro.families.Dihedral(17)

	list_groups = [C3, C4, C6, D4, D17]
	
	for i, Gi in enumerate(list_groups):
		for j, Gj in enumerate(list_groups):
			assert (i==j) == (fingro.isomorphic(Gi, Gj))
