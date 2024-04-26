import fingro
from itertools import product
import numpy as np

class DirectProduct(fingro.Group):
	def __init__(self, G1: fingro.Group, G2: fingro.Group):

		self.G1 = G1
		self.G2 = G2
		
		indexes = tuple(product(range(len(G1)), range(len(G2))))

		matrix = np.array([
			[indexes.index((G1.matrix[i1, j1], G2.matrix[i2,j2]))
				for j1, j2 in indexes]
					for i1, i2 in indexes
		])

		element_names = [
			f'{G1.element_names[i]}, {G2.element_names[j]}'
				for i, j in indexes
		]

		super().__init__(
			matrix=matrix,
			name=f'{G1.name}×{G2.name}',
			elements=tuple(product(G1.elements, G2.elements)),
			element_names=element_names,
			check_matrix_type_and_shape=False,
			check_group_properties=False,
		)

	# TODO: This is not a correct implementation. 
	# C2 * C7 has only one generator.
	@property
	def generators(self):
		if self._generators == None:
			self._generators = (
				self.G1.generators
				+ tuple(len(self.G2) * i for i in self.G2.generators)
			)
		return self._generators
