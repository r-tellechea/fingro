import numpy as np
import plotly.express as px

from fingro.groups import Element

class Group:
	def __init__(self, 
		
		matrix: np.ndarray,
		element_names: list[str]=None,
		check_matrix_type_and_shape: bool=True,
		check_group_properties: bool=True,
		check_abelian: bool=False,
		
		):

		# TODO: Check matrix type and shape
		
		self.matrix = matrix
		self.order = self.matrix.shape[0]

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

		self.abelian = False
		if check_abelian:
			self.check_abelian()
	
	def check_group_properties(self):
		# Check neutral element.
		if not (self.matrix[:, 0].ravel() == np.arange(self.order)).all():
			raise ValueError('Property: Neutral element.')
		
		# Check inverse element.
		if not ((self.matrix == 0).sum(axis=0) == 1).all():
			raise ValueError('Property: Inverse element.')

		# Check associativity.
		for i in range(self.order):
			for j in range(self.order):
				for k in range(self.order):
					ij = self.matrix[i, j]
					jk = self.matrix[j, k]
					if self.matrix[ij, k] != self.matrix[i, jk]:
						raise ValueError(f'Property: Associativity. ({i=}, {j=}, {k=})')

	def check_abelian(self):
		for i in range(self.order):
			for j in range(self.order):
				if self.matrix[i,j] != self.matrix[j,i]:
					return None
		self.abelian = True

	# TODO: Hoverplate: xy = self.elements[index]
	def fig(self, color_continuous_scale: str='deep'):
		fig = px.imshow(
			self.matrix,
			color_continuous_scale='deep',
			x=self.element_names,
			y=self.element_names,
			labels={'color' : 'xy'},
		)
		fig.update_xaxes(
			title = 'x',
			title_font = {'size': 20},
			tickfont = {'size': 20},
			side = 'top'
		)
		fig.update_yaxes(
			title = 'y',
			title_font = {'size': 20},
			tickfont = {'size': 20},
			side = 'left'
		)
		fig.update_layout(
			coloraxis_showscale=False,
			margin=dict(l=0, r=0, b=30, t=0),
			width=500
		)
		return fig

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