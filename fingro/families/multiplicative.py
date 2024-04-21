import fingro
from math import gcd
import numpy as np

class Multiplicative(fingro.Group):
	def __init__(self, n: int):
		coprimes = [m for m in range(1, n) if gcd(m,n) == 1]
		matrix = np.array([
			[coprimes.index((m1 * m2) % n)
				for m2 in coprimes]		
					for m1 in coprimes
		])
		
		element_names = [str(m) for m in coprimes]

		super().__init__(
			matrix=matrix,
			element_names=element_names,
			name=f'U{len(coprimes)}',
			check_matrix_type_and_shape=True,
			check_group_properties=True,
			check_abelian=False,
		)

		self.abelian = True
