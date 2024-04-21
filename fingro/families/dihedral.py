import fingro
import numpy as np

class Dihedral(fingro.Group):
	
	def __init__(self, k: int):
	
		cyclic_matrix = np.mod(
			np.arange(k) + np.arange(k).reshape((-1,1)), 
			k
		)
		matrix = np.concatenate([
			np.concatenate([cyclic_matrix, cyclic_matrix + k], axis=1),
			np.concatenate([cyclic_matrix + k, cyclic_matrix], axis=1)
			], axis=0)
		element_names = (
			  ['1', 'σ'] 
			+ [f'σ{i}' for i in range(2, k)]
			+ ['τ', 'τσ']
			+ [f'τσ{i}' for i in range(2, k)]
		)
		
		super().__init__(
			matrix=matrix,
			element_names=element_names,
			check_matrix_type_and_shape=False,
			check_group_properties=False,
			check_abelian=False
		)
		
		self.abelian=(False if k == 1 else True)
