import fingro
from itertools import product
import numpy as np

class DirectProduct(fingro.Group):
	def __init__(self, G: fingro.Group, H: fingro.Group):
		
		indexes = tuple(product(range(len(G)), range(len(H))))

		matrix = np.array([
			[indexes.index((G.matrix[i1, j1], H.matrix[i2,j2]))
				for j1, j2 in indexes]
					for i1, i2 in indexes
		])

		element_names = [
			f'{G.element_names[i]}, {H.element_names[j]}'
				for i, j in indexes
		]

		super().__init__(
			matrix=matrix,
			element_names=element_names,
			check_matrix_type_and_shape=False,
			check_group_properties=False,
			check_abelian=False,
		)

		if isinstance(G.abelian, bool) and isinstance(H.abelian, bool):
			self.abelian = G.abelian and H.abelian
		else:
			self.abelian = None
