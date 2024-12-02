import fingro
import numpy as np

def test_init():
	C8_family = fingro.families.Cyclic(8)
	C8_manual = fingro.Group(
		matrix=np.array([
			[0,1,2,3, 4,5,6,7],
			[1,2,3,4, 5,6,7,0],
			[2,3,4,5, 6,7,0,1],
			[3,4,5,6, 7,0,1,2],
			
			[4,5,6,7, 0,1,2,3],
			[5,6,7,0, 1,2,3,4],
			[6,7,0,1, 2,3,4,5],
			[7,0,1,2, 3,4,5,6],
		]),
		element_names=[str(i) for i in range(8)],
		name='C8_manual',
		check_matrix_type_and_shape=False,
		check_group_properties=False,
	)
	assert C8_family == C8_manual
	C8_family.check_matrix_type_and_shape()
	C8_family.check_group_properties()

def test_properties():
	assert fingro.families.Cyclic(8).abelian
