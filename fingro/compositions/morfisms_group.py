import fingro
from typing import Callable
import numpy as np

class MorfismsGroup(fingro.Group):
	def __init__(
		
		self, 
		dom: fingro.Group, 
		cod: fingro.Group,
		name: str,
		get_morfisms_fn: Callable,

		):
		
		self.dom = dom
		self.cod = cod
		self.morfisms = get_morfisms_fn(self.dom, self.cod)

		super().__init__(
			matrix=np.array([
				[self.morfisms.index(f1 * f2)
					for f2 in self.morfisms]
						for f1 in self.morfisms
			]),
			element_names=[f.name for f in self.morfisms],
			name=f'{name}({self.dom.name}, {self.cod.name})',
			check_matrix_type_and_shape=False,
			check_group_properties=False
		)

class HomomorfismsGroup(MorfismsGroup):
	def __init__(self, dom: fingro.Group, cod: fingro.Group):
		super().__init__(
			dom=dom,
			cod=cod,
			name='Hom',
			get_morfisms_fn=(
				fingro
				.compositions
				.compose_functions
				.get_homomorfisms
			)
		)

class EndomorfismsGroup(MorfismsGroup):
	def __init__(self, group: fingro.Group):
		self.group = group
		super().__init__(
			dom=self.group,
			cod=self.group,
			name='End',
			get_morfisms_fn=(
				fingro
				.compositions
				.compose_functions
				.get_homomorfisms
			)
		)

# TODO: Isomorfisms group is group under homomorfism composition, not product.
class IsomorfismsGroup(MorfismsGroup):
	def __init__(self, dom: fingro.Group, cod: fingro.Group):
		super().__init__(
			dom=dom,
			cod=cod,
			name='Iso',
			get_morfisms_fn=(
				fingro
				.compositions
				.compose_functions
				.get_isomorfisms
			)
		)

# TODO: Automorfisms group is group under homomorfism composition, not product.
class AutomorfismsGroup(MorfismsGroup):
	def __init__(self, group: fingro.Group):
		self.group = group
		super().__init__(
			dom=self.group,
			cod=self.group,
			name='Aut',
			get_morfisms_fn=(
				fingro
				.compositions
				.compose_functions
				.get_isomorfisms
			)
		)
