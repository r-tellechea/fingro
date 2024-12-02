import fingro
import numpy as np

def test_init():
	D4_family = fingro.families.Dihedral(4)
	D4_manual = fingro.Group(
		matrix=np.array([
			[0,1,2,3, 4,5,6,7],
			[1,2,3,0, 7,4,5,6],
			[2,3,0,1, 6,7,4,5],
			[3,0,1,2, 5,6,7,4],

			[4,5,6,7, 0,1,2,3],
			[5,6,7,4, 3,0,1,2],
			[6,7,4,5, 2,3,0,1],
			[7,4,5,6, 1,2,3,0]
		]),
		element_names=[str(i) for i in range(8)],
		name='D4_manual',
		check_matrix_type_and_shape=False,
		check_group_properties=False,
	)
	assert D4_family == D4_manual
	D4_family.check_matrix_type_and_shape()
	D4_family.check_group_properties()

def test_properties():
	assert fingro.families.Dihedral(2).abelian
	assert not fingro.families.Dihedral(3).abelian
	assert not fingro.families.Dihedral(4).abelian
