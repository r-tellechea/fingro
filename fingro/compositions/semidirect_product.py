import fingro
import numpy as np
from itertools import product

class SemidirectProduct(fingro.Group):
	def __init__(self, 
		H: fingro.Group, 
		N: fingro.Group, 
		phi: fingro.Homomorphism, 
		check_homomorphism: bool=True ):

		if check_homomorphism:
		
			if not fingro.same_matrix(phi.dom, H):
				raise ValueError('The domain of phi is not H.')
				
			if not fingro.same_matrix(phi.cod, fingro.compositions.AutomorphismsGroup(N)):
				raise ValueError('The codomain of phi is not Aut(N).')

		group_order = len(H) * len(N)

		index = np.arange(group_order).reshape(len(H), len(N))
		
		g1 = index.reshape((-1,1))
		g2 = index.reshape((1,-1))

		h1 = np.broadcast_to(g1 // len(N), (group_order, group_order))
		h2 = np.broadcast_to(g2 // len(N), (group_order, group_order))
		
		n1 = np.broadcast_to(g1 %  len(N), (group_order, group_order))
		n2 = np.broadcast_to(g2 %  len(N), (group_order, group_order))

		induced_hom = np.array([phi.cod.elements[i].f for i in phi.f])

		matrix = index[
			H.matrix[h1, h2], 
			N.matrix[n1, induced_hom[h1, n2]]
		]

		super().__init__(
			matrix=matrix,
			name=f'{N.name}⋊{H.name}',
			elements=tuple(product(H.elements, N.elements)),
			element_names=tuple(
				f'{name_h}, {name_n}' 
					for name_n in N.element_names
						for name_h in H.element_names
			),
			check_matrix_type_and_shape=False,
			check_group_properties=False,
		)
