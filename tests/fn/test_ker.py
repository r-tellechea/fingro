import fingro
import numpy as np

def test_ker():
	C4 = fingro.families.Cyclic(4)
	C8 = fingro.families.Cyclic(8)
	f = fingro.Homomorphism(
		f=(np.arange(8) % 4),
		dom=C8, cod=C4,
		check_homomorphism=False
	)
	ker = fingro.fn.ker(f)
	assert ker == fingro.families.Cyclic(2)
	assert ker.sub_index == (0,4)

	D4 = fingro.families.Dihedral(4)
	D8 = fingro.families.Dihedral(8)
	f = fingro.Homomorphism(
		f=(np.arange(8) * 2),
		dom=D4, cod=D8,
		check_homomorphism=False
	)
	ker = fingro.fn.ker(f)
	assert ker == fingro.families.Cyclic(1)
	assert ker.sub_index == (0,)
