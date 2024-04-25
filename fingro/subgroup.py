import fingro
import numpy as np

class Subgroup(fingro.Group):

	####################
	# Initialization.
	####################

	def __init__(self, 
		
		group: fingro.Group,
		sub_index: tuple[int],
		name: str=None,
		
		):

		self.group = group
		self.sub_index = sub_index
		self.not_sub_index = tuple(
			set(range(len(self.group)))
			- set(self.sub_index)
		)

		try:
			matrix = np.array([
				[self.sub_index.index(self.group.matrix[i,j])
					for j in sub_index]
						for i in sub_index
			])
		except:
			raise ValueError('Not a subgroup.')
		
		element_names=tuple(
			self.group.element_names[i] 
				for i in self.sub_index
		)

		super().__init__(
			matrix=matrix,
			element_names=tuple(
				self.group.element_names[i] 
					for i in self.sub_index
			),
			name=name if name != None else f'{self.group.name}_{element_names}',
			check_matrix_type_and_shape=False,
			check_group_properties=False,
		)

		self._normal = None
		self._inclusion = None

	####################
	# Properties.
	####################

	@property
	def normal(self):
		if self._normal == None:
			self._normal = fingro.fn.normal(group=self.group, subgroup=self)
		return self._normal

	@normal.setter
	def normal(self, value):
		self._normal = value 

	# TODO: Check normal.
	def check_normal(self):
		pass

	@property
	def inclusion(self):
		if self._inclusion == None:
			self.build_inclusion()
		return self._inclusion
	
	def build_inclusion(self):
		self._inclusion = fingro.Homomorphism(
			f=np.array(self.sub_index),
			dom=self,
			cod=self.group,
			name=f'{self.name}↣{self.group.name}',
			check_homomorphism=False,
		)
		
		self._inclusion.inj = True
		self._inclusion.sur = len(self) == len(self.group)

	####################
	# Arithmetic.
	####################

	def __and__(self, other):
		if not fingro.fn.same_matrix(self.group, other.group):
			raise ValueError('Not subgroups of the same group.')
		return fingro.Subgroup(
			group=self.group,
			sub_index=tuple( i for i in self.sub_index if i in other.sub_index ),
		)

	def __or__(self, other):
		if not fingro.fn.same_matrix(self.group, other.group):
			raise ValueError('Not subgroups of the same group.')
		return fingro.fn.generated_subgroup(
			group=self.group,
			index=tuple(set(self.sub_index) | set(other.sub_index))
		)

	####################
	# Relations.
	####################

	def __eq__(self, other) -> bool:
		if isinstance(other, fingro.Subgroup):
			same_group = fingro.fn.same_matrix(self.group, other.group)
			same_index = set(self.sub_index) == set(other.sub_index)
			if same_group and same_index:
				return True
		return super().__eq__(other)

	def __lt__(self, other) -> bool:
		if isinstance(other, fingro.Subgroup):
			same_group = fingro.fn.same_matrix(self.group, other.group)
			same_index = set(self.sub_index) <= set(other.sub_index)
			if same_group and same_index:
				return True
		return super().__lt__(other)
