import fingro
import numpy as np

def test_init():
	M5_family = fingro.families.Multiplicative(5)
	M5_manual = fingro.Group(
		matrix=np.array([
			[0,1,2,3],
			[1,3,0,2],
			[2,0,3,1],
			[3,2,1,0],
		]),
		element_names=[str(i) for i in range(4)],
		name='M5_manual',
		check_matrix_type_and_shape=False,
		check_group_properties=False,
	)
	assert M5_family == M5_manual
	M5_family.check_matrix_type_and_shape()
	M5_family.check_group_properties()

def test_properties():
	assert fingro.families.Multiplicative(5).abelian
	assert fingro.families.Multiplicative(17).abelian
	assert fingro.families.Multiplicative(67).abelian
