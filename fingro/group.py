import fingro
from dataclasses import dataclass
import numpy as np
import plotly.express as px

class Group:

	####################
	# Initialization.
	####################

	def __init__(self, 
		
		matrix: np.ndarray,
		name: str='G',
		elements: tuple|None=None,
		element_names: tuple[str]=None,
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
		self.element_inverses = np.argmin(self.matrix, axis=1)
	
		# Properties
		self._abelian = None
		self._generators = None
		self._elements = None
		self.elements = elements
	
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
	def abelian(self, value: bool):
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
	
	@property
	def generators(self):
		if self._generators == None:
			self._generators = fingro.fn.generators(self)
		return self._generators

	@generators.setter
	def generators(self, index: tuple[int]):
		if len(self) != len(fingro.generated_subgroup(self, index)):
			raise ValueError('This index of elements does not generate the group.')
		self._generators = index

	@property
	def elements(self):
		if self._elements == None:
			pass
		return self._elements

	@elements.setter
	def elements(self, elements: tuple | None):
		if elements == None:
			return
		if len(elements) != len(self):
			raise ValueError('Not as many elements as the group order.')
		self._elements = elements if isinstance(elements, tuple) else tuple(elements)

	def __len__(self):
		return self.order

	####################
	# Visualization.
	####################

	def __str__(self) -> str:
		return self.name

	# TODO: Hoverplate: xy = self.element_names[index]
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
	# Arithmetic.
	####################

	def __mul__(self, other):
		return fingro.compositions.DirectProduct(self, other)

	def __xor__(self, other):
		return fingro.compositions.HomomorphismsGroup(self, other)

	def __truediv__(self, other):
		return fingro.compositions.QuotientGroup(self, other)

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
