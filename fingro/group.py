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
		if hash(self.group) != hash(other.group):
			raise ValueError('Operating elements from diferent groups.')
		return self.group.elements[self.group.matrix[self.i, other.i]]

class Group:
	def __init__(self, 
		
		matrix: np.ndarray,
		element_names: list[str]=None,
		name: str='G',
		check_matrix_type_and_shape: bool=True,
		check_group_properties: bool=True,
		
		):

		# TODO: Check matrix type and shape
		
		self.matrix = matrix
		self.order = self.matrix.shape[0]
		self.name = name

		self.element_names = element_names if element_names != None else list(map(str, range(self.order)))
		self.element_orders = [
			self.get_index_order(i)
				for i in range(self.order)
		]
		self.elements = [
			Element(i, name, order, self)
				for i, name, order in zip(
					range(self.order), 
					self.element_names, 
					self.element_orders
				)
		]

		self._abelian = None
	
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

	def __str__(self) -> str:
		return self.name

	def __len__(self):
		return self.order
	
	def __hash__(self):
		return hash(tuple(self.matrix.ravel()))
	
	def __iter__(self):
		for element in self.elements:
			yield element

	def get_index_order(self, index: int):
		current_index = index
		order = 1
		while current_index != 0:
			current_index = self.matrix[current_index, index]
			order += 1
		return order

	def center(self):
		tup_conmute = (self.matrix == self.matrix.T).all(axis=0)
		center_index = tuple( 
			i
				for i, conmute in enumerate(tup_conmute) 
					if conmute
		)
		center = fingro.Subgroup(
			group=self,
			sub_index=center_index,
			name=f'Z({self.name})',
		)
		center.normal = True
		center.abelian = True
		return center
