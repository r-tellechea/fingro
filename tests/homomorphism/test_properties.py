import fingro
import numpy as np

def test_inj():
	C2 = fingro.families.Cyclic(2)
	C4 = fingro.families.Cyclic(4)
	
	f1 = fingro.Homomorphism(
		f=(np.arange(2) * 2),
		dom=C2, cod=C4,
		check_homomorphism=False
	)
	f2 = fingro.Homomorphism(
		f=(np.arange(4) % 2),
		dom=C4, cod=C2,
		check_homomorphism=False
	)

	assert f1.inj
	assert not f2.inj

def test_sur():
	C2 = fingro.families.Cyclic(2)
	C4 = fingro.families.Cyclic(4)
	
	f1 = fingro.Homomorphism(
		f=(np.arange(2) * 2),
		dom=C2, cod=C4,
		check_homomorphism=False
	)
	f2 = fingro.Homomorphism(
		f=(np.arange(4) % 2),
		dom=C4, cod=C2,
		check_homomorphism=False
	)

	assert not f1.sur
	assert f2.sur

def test_bij():
	C4 = fingro.families.Cyclic(4)
	
	f1 = fingro.Homomorphism(
		f=np.arange(4),
		dom=C4, cod=C4,
		check_homomorphism=False
	)
	f2 = fingro.Homomorphism(
		f=((np.arange(4) * 2) % 4),
		dom=C4, cod=C4,
		check_homomorphism=False
	)

	assert f1.bij
	assert not f2.bij

def test_ker():
	C2 = fingro.families.Cyclic(2)
	C4 = fingro.families.Cyclic(4)
	
	f1 = fingro.Homomorphism(
		f=(np.arange(2) * 2),
		dom=C2, cod=C4,
		check_homomorphism=False
	)
	f2 = fingro.Homomorphism(
		f=(np.arange(4) % 2),
		dom=C4, cod=C2,
		check_homomorphism=False
	)
	
	assert f1.ker == fingro.fn.ker(f1)
	assert f2.ker == fingro.fn.ker(f2)


def test_im():
	C2 = fingro.families.Cyclic(2)
	C4 = fingro.families.Cyclic(4)
	
	f1 = fingro.Homomorphism(
		f=(np.arange(2) * 2),
		dom=C2, cod=C4,
		check_homomorphism=False
	)
	f2 = fingro.Homomorphism(
		f=(np.arange(4) % 2),
		dom=C4, cod=C2,
		check_homomorphism=False
	)

	assert f1.im == fingro.fn.im(f1)
	assert f2.im == fingro.fn.im(f2)
