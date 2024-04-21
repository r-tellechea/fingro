import fingro
import numpy as np

class Subgroup(fingro.Group):
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

		self.inclusion = fingro.morfisms.Homomorfism(
			f = lambda i : self.sub_index[i],
			dom=self,
			cod=self.group,
			name=f'{self.name}↣{self.group.name}',
			check_homomorfism=False,
		)
		
		self.inclusion.inj = True
		self.inclusion.sur = len(self) == len(self.group)

		self._normal = None

	@property
	def normal(self):
		if self._normal == None:
			self.check_normal()
		return self._normal

	# TODO: Check normal.
	def check_normal(self):
		pass
