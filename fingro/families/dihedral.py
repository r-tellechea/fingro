import fingro
import numpy as np

class Dihedral(fingro.Group):
	
	def __init__(self, k: int):
	
		i = np.arange(k).reshape((-1,1))
		j = np.arange(k)
		ij = np.mod(i + j, k)
		ji = np.mod(j - i, k)

		matrix = np.concatenate([
			np.concatenate([ij, ji + k], axis=1),
			np.concatenate([ij + k, ji], axis=1)
			], axis=0)
		element_names = (
			  ['1', 'σ'] 
			+ [f'σ{i}' for i in range(2, k)]
			+ ['τ', 'τσ']
			+ [f'τσ{i}' for i in range(2, k)]
		)
		
		super().__init__(
			matrix=matrix,
			name=f'D{k}',
			elements=tuple(range(2*k)),
			element_names=element_names,
			check_matrix_type_and_shape=False,
			check_group_properties=False,
		)
		
		self._abelian = (k < 3)
		self._generators = (1, k)
