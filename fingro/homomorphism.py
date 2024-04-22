import fingro
from typing import Callable
from functools import reduce
import numpy as np

class Homomorphism:

	####################
	# Initialization.
	####################
	
	def __init__(self, 
	
		f: Callable[int, int], 
		dom: fingro.Group, 
		cod: fingro.Group,
		name: str='f',
		check_homomorphism: bool=True,

		):

		self.f = { i : f(i) for i in range(dom.order) }
		self.dom = dom
		self.cod = cod
		self.name = name

		if check_homomorphism:
			self.check_homomorphism()
		
		self._inj = None
		self._sur = None
		self._bij = None

	def check_homomorphism(self):
		for g in self.dom:
			for h in self.dom:
				if self(g * h) != self(g) * self(h):
					raise ValueError(f'Not homomorphism: f({g} * {h}) ≠ f({g}) * f({h})')

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
		self.inj = len([i for i in self.f.values() if i == 0]) == 1

	def check_surjective(self):
		self.sur = len(set(self.f.values())) == len(self.cod)

	####################
	# Visualization.
	####################

	def __str__(self) -> str:
		return reduce(
			lambda x, y : f'{x}\n{y}',
			map(
				lambda g : f'{self.name}({g}) = {self(g)}',
				self.dom
			)
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
			f=( lambda i : self.cod.matrix[self.f[i], other.f[i]] ),
			dom=self.dom,
			cod=self.cod,
			name=f'{self.name} * {other.name}',
			check_homomorphism=False
		)

	def __matmul__(self, other):
		
		if not self.cod == other.dom:
			raise ValueError(f'{self.name} codomain is not {other.name} domain.')

		return Homomorphism(
			f=( lambda i : other.f[self.f[i]] ),
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
	
	def __call__(self, g: fingro.Element) -> fingro.Element:
		return self.cod.elements[self.f[g.i]]

	####################
	# Subgroups.
	####################

	def ker(self) -> fingro.Subgroup:
		return fingro.ker(self)

	def im(self) -> fingro.Subgroup:
		return fingro.im(self)
