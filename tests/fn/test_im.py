import fingro
import numpy as np

def test_im():
	C4 = fingro.families.Cyclic(4)
	C8 = fingro.families.Cyclic(8)
	f = fingro.Homomorphism(
		f=np.zeros((8,), dtype='int'),
		dom=C8, cod=C4,
		check_homomorphism=True
	)
	im = fingro.fn.im(f)
	assert im == fingro.families.Cyclic(1)
	assert im.sub_index == (0,)

	D4 = fingro.families.Dihedral(4)
	D8 = fingro.families.Dihedral(8)
	f = fingro.Homomorphism(
		f=(np.arange(8) * 2),
		dom=D4, cod=D8,
		check_homomorphism=True
	)
	im = fingro.fn.im(f)
	assert im == D4
	assert im.sub_index == tuple(range(0, 16, 2))
