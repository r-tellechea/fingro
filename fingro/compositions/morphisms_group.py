import fingro
from typing import Callable
import numpy as np

class morphismsGroup(fingro.Group):
	def __init__(
		
		self, 
		dom: fingro.Group, 
		cod: fingro.Group,
		name: str,
		get_morphisms_fn: Callable[tuple[fingro.Group], list[fingro.Homomorphism]],
		morphism_operation: Callable[tuple[fingro.Homomorphism], fingro.Homomorphism],

		):
		
		self.dom = dom
		self.cod = cod
		self.morphisms = tuple(get_morphisms_fn(self.dom, self.cod))

		super().__init__(
			matrix=np.array([
				[self.morphisms.index(morphism_operation(f1, f2))
					for f2 in self.morphisms]
						for f1 in self.morphisms
			]),
			element_names=[f.name for f in self.morphisms],
			name=f'{name}({self.dom.name}, {self.cod.name})',
			check_matrix_type_and_shape=False,
			check_group_properties=False
		)

class HomomorphismsGroup(morphismsGroup):
	def __init__(self, dom: fingro.Group, cod: fingro.Group):
		super().__init__(
			dom=dom,
			cod=cod,
			name='Hom',
			get_morphisms_fn=(
				fingro
				.compositions
				.compose_functions
				.get_homomorphisms
			),
			morphism_operation=(lambda f1, f2: f1 * f2),
		)

class EndomorphismsGroup(morphismsGroup):
	def __init__(self, group: fingro.Group):
		self.group = group
		super().__init__(
			dom=self.group,
			cod=self.group,
			name='End',
			get_morphisms_fn=(
				fingro
				.compositions
				.compose_functions
				.get_homomorphisms
			),
			morphism_operation=(lambda f1, f2: f1 * f2),
		)

class IsomorphismsGroup(morphismsGroup):
	def __init__(self, dom: fingro.Group, cod: fingro.Group):
		super().__init__(
			dom=dom,
			cod=cod,
			name='Iso',
			get_morphisms_fn=(
				fingro
				.compositions
				.compose_functions
				.get_isomorphisms
			),
			morphism_operation=(lambda f1, f2: f1 @ f2),
		)

class AutomorphismsGroup(morphismsGroup):
	def __init__(self, group: fingro.Group):
		self.group = group
		super().__init__(
			dom=self.group,
			cod=self.group,
			name='Aut',
			get_morphisms_fn=(
				fingro
				.compositions
				.compose_functions
				.get_isomorphisms
			),
			morphism_operation=(lambda f1, f2: f1 @ f2),
		)
