import fingro

def test_correct_subgroup():
	D4 = fingro.families.Dihedral(4)
	fingro.Subgroup(D4, sub_index=(0,1,2,3))

def test_incorrect_subgroup():
	D4 = fingro.families.Dihedral(4)
	try:
		fingro.Subgroup(D4, sub_index=(0,1))
	except ValueError as e:
		assert str(e) == 'Not a subgroup.'
