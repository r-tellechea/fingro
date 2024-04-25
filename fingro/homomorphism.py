import fingro
from typing import Callable
from functools import reduce
import numpy as np

class Homomorphism:

	####################
	# Initialization.
	####################
	
	def __init__(self, 
	
		f: np.ndarray, 
		dom: fingro.Group, 
		cod: fingro.Group,
		name: str='f',
		check_homomorphism: bool=True,

		):

		self.f = f
		self.dom = dom
		self.cod = cod
		self.name = name

		if check_homomorphism:
			self.check_homomorphism()
		
		self._inj = None
		self._sur = None
		self._bij = None

		self._ker = None
		self._im  = None

	def check_homomorphism(self):
		
		index_dom = np.arange(len(self.dom))
		
		homomorphism_condition = np.array_equal(
			self(self.dom.matrix),

			self.cod.matrix
			[self(index_dom),:]
			[:,self(index_dom)]			
		)

		if not homomorphism_condition:
			raise ValueError('Not homomorphism.')

	####################
	# Properties.
	####################

	@property
	def inj(self):
		if self._inj == None:
			self.check_injective()
		return self._inj

	@property
	def sur(self):
		if self._sur == None:
			self.check_surjective()
		return self._sur
	
	@property
	def bij(self):
		if self._bij == None:
			self._bij = self.inj and self.sur
		return self._bij

	@inj.setter
	def inj(self, value):
		self._inj = value

	@sur.setter
	def sur(self, value):
		self._sur = value

	@bij.setter
	def bij(self, value):
		self._bij = value 

	def check_injective(self):
		self.inj = (self.f == 0).sum() == 1

	def check_surjective(self):
		self.sur = len(set(self.f)) == len(self.cod)

	@property
	def ker(self):
		if self._ker == None:
			self._ker = fingro.ker(self)
		return self._ker

	@property
	def im(self):
		if self._im == None:
			self._im = fingro.im(self)
		return self._im

	####################
	# Visualization.
	####################

	def __str__(self) -> str:
		return reduce(
			lambda x, y : f'{x}\n{y}',
			(f'{self.name}({self.dom.element_names[i]}) = {self.cod.element_names[fi]}'
				for i, fi in enumerate(self.f))
		)
	
	####################
	# Arithmetic.
	####################

	def __mul__(self, other):
		
		if not self.dom == other.dom:
			raise ValueError('Not the same domain.')
		
		if not self.cod == other.cod:
			raise ValueError('Not the same codomain.')
		
		return Homomorphism(
			f=self.cod.matrix[self.f, other.f],
			dom=self.dom,
			cod=self.cod,
			name=f'{self.name} * {other.name}',
			check_homomorphism=False
		)

	def __matmul__(self, other):
		
		if not self.cod == other.dom:
			raise ValueError(f'{self.name} codomain is not {other.name} domain.')

		return Homomorphism(
			f=other.f[self.f],
			dom=self.dom,
			cod=other.cod,
			name=f'{self.name} @ {other.name}',
			check_homomorphism=False
		)

	####################
	# Relations.
	####################
	
	def __eq__(self, other) -> bool:
		
		if not self.dom == other.dom:
			raise ValueError('Not the same domain.')
		
		if not self.cod == other.cod:
			raise ValueError('Not the same codomain.')

		return all( self.f[i] == other.f[i] for i in range(len(self.dom)) )
	
	def __ne__(self, other) -> bool:
		return not self == other

	####################
	# Function.
	####################
	
	def __call__(self, i: int|np.ndarray) -> int:
		return self.f[i]
