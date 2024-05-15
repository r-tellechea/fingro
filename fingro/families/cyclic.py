import fingro
import numpy as np

class Cyclic(fingro.Group):
	
	def __init__(self, order: int):
		
		matrix = np.mod(
			np.arange(order) + np.arange(order).reshape((-1,1)), 
			order
		)

		element_names = ['1', 'g'] + [f'g{i}' for i in range(2, order)] if order != 1 else ['1']
		
		super().__init__(
			matrix=matrix,
			name=f'C{order}',
			elements=tuple(range(order)),
			element_names=element_names,
			check_matrix_type_and_shape=False,
			check_group_properties=False,
		)
		
		self._abelian = True
		self._generators = (1,) if order != 1 else (0,)
