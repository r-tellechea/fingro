import fingro
from dataclasses import dataclass
import numpy as np
import plotly.express as px

@dataclass
class Element:
	i: int
	name: str
	order: int
	group: 'Group'

	def __str__(self) -> str:
		return self.name
	
	def __mul__(self, other: 'Element') -> 'Element':
		if not fingro.same_matrix(self.group, other.group):
			raise ValueError('Operating elements from diferent groups.')
		return self.group.elements[self.group.matrix[self.i, other.i]]

class Group:

	####################
	# Initialization.
	####################

	def __init__(self, 
		
		matrix: np.ndarray,
		element_names: tuple[str]=None,
		name: str='G',
		check_matrix_type_and_shape: bool=True,
		check_group_properties: bool=True,
		
		):

		self.matrix = matrix
		self.order = self.matrix.shape[0]
		self.name = name

		if check_matrix_type_and_shape:
			self.check_matrix_type_and_shape()

		if check_group_properties:
			self.check_group_properties()

		self.element_names = element_names if element_names != None else tuple(map(str, range(self.order)))
		self.element_orders = tuple(
			self.get_index_order(i)
				for i in range(self.order)
		)
		self.elements = tuple(
			Element(i, name, order, self)
				for i, name, order in zip(
					range(self.order), 
					self.element_names, 
					self.element_orders
				)
		)
		self.element_inverses = np.argmin(self.matrix, axis=1)
	
		self._abelian = None
	
	# TODO: Check matrix type and shape
	def check_matrix_type_and_shape(self):
		pass
	
	def check_group_properties(self):
		# Check neutral element.
		if not (self.matrix[:, 0].ravel() == np.arange(self.order)).all():
			raise ValueError('Property: Neutral element.')
		
		# Check inverse element.
		if not ((self.matrix == 0).sum(axis=0) == 1).all():
			raise ValueError('Property: Inverse element.')

		# Check associativity.
		if not np.array_equal(self.matrix[self.matrix, :], self.matrix[:, self.matrix]):
			raise ValueError('Property: Associativity.')

	####################
	# Properties.
	####################

	@property
	def abelian(self):
		if self._abelian == None:
			self.check_abelian()
		return self._abelian

	@abelian.setter
	def abelian(self, value):
		self._abelian = value 

	def check_abelian(self):
		self._abelian = np.array_equal(self.matrix, self.matrix.T)

	def get_index_order(self, index: int):
		current_index = index
		order = 1
		while current_index != 0:
			current_index = self.matrix[current_index, index]
			order += 1
		return order

	def __len__(self):
		return self.order

	####################
	# Visualization.
	####################

	def __str__(self) -> str:
		return self.name

	# TODO: Hoverplate: xy = self.elements[index]
	def fig(self, color_continuous_scale: str='deep'):
		fig = px.imshow(
			self.matrix,
			color_continuous_scale='deep',
			x=self.element_names,
			y=self.element_names,
			labels={'color' : 'xy'},
			title=self.name,
		)
		fig.update_xaxes(
			title = 'y',
			title_font = {'size': 20},
			tickfont = {'size': 20},
			side = 'top'
		)
		fig.update_yaxes(
			title = 'x',
			title_font = {'size': 20},
			tickfont = {'size': 20},
			side = 'left'
		)
		fig.update_layout(
			coloraxis_showscale=False,
			margin=dict(l=0, r=0, b=30, t=0),
			width=500,
			title=dict(font=dict(size=25))
		)
		return fig

	####################
	# Elements.
	####################

	def __iter__(self):
		for element in self.elements:
			yield element

	####################
	# Arithmetic.
	####################

	def __mul__(self, other):
		return fingro.compositions.DirectProduct(self, other)

	def __xor__(self, other):
		return fingro.compositions.HomomorphismsGroup(self, other)

	####################
	# Relations.
	####################

	def __eq__(self, other) -> bool:
		return fingro.isomorphic(self, other)

	def __ne__(self, other) -> bool:
		return not self == other

	def __lt__(self, other) -> bool:
		return fingro.is_subgroup(self, other)
	
	def __le__(self, other) -> bool:
		return self < other

	def __gt__(self, other) -> bool:
		return other < self
	
	def __ge__(self, other) -> bool:
		return other < self
