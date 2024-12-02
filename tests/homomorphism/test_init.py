import fingro
import numpy as np

def test_check_homomorfism():
	C4 = fingro.families.Cyclic(4)
	C8 = fingro.families.Cyclic(8)
	
	fingro.Homomorphism(
		f=(np.arange(8) % 4),
		dom=C8, cod=C4,
		check_homomorphism=True
	)
	
	try:
		fingro.Homomorphism(
			f=(np.arange(8) // 2),
			dom=C8, cod=C4,
			check_homomorphism=True
		)
		assert False
	except ValueError as e:
		assert str(e) == 'Not homomorphism.'
