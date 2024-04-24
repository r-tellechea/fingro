import fingro
import numpy as np

class Cyclic(fingro.Group):
	
	def __init__(self, order: int):
		
		matrix = np.mod(
			np.arange(order) + np.arange(order).reshape((-1,1)), 
			order
		)

		element_names = ['1', 'g'] + [f'g{i}' for i in range(2, order)]
		
		super().__init__(
			matrix=matrix,
			element_names=element_names,
			name=f'C{order}',
			check_matrix_type_and_shape=False,
			check_group_properties=False,
		)
		
		self._abelian = True
		self._generators = (1,)
