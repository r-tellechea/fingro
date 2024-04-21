import fingro
from typing import Callable
from functools import reduce
import numpy as np

class Homomorfism:
	def __init__(self, 
	
		f: Callable[int, int], 
		dom: fingro.Group, 
		cod: fingro.Group,
		name: str='f',
		check_homomorfism: bool=True,

		):

		self.f = { i : f(i) for i in range(dom.order) }
		self.dom = dom
		self.cod = cod
		self.name = name

		if check_homomorfism:
			self.check_homomorfism()
		
		self._inj = None
		self._sur = None
		self._bij = None

	def check_homomorfism(self):
		for g in self.dom:
			for h in self.dom:
				if self(g * h) != self(g) * self(h):
					raise ValueError(f'Not homomorfism: f({g} * {h}) ≠ f({g}) * f({h})')

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

	def check_injective(self):
		self.inj = len([i for i in self.f.values() if i == 0]) == 1

	def check_surjective(self):
		self.sur = len(set(self.f.values())) == len(self.cod)
	
	def ker(self) -> fingro.Subgroup:
		return fingro.Subgroup(
			group=self.dom,
			sub_index=tuple( i for i in range(len(self.dom)) if self.f(i) == 0 ),
			name=f'ker({self.name})',
		)

	def im(self) -> fingro.Subgroup:
		return fingro.Subgroup(
			group=self.cod,
			sub_index=tuple(set(f(i) for i in range(len(self.dom)))),
			name=f'im({self.name})',
		)

	def __call__(self, g: fingro.Element) -> fingro.Element:
		return self.cod.elements[self.f[g.i]]

	def __str__(self) -> str:
		return reduce(
			lambda x, y : f'{x}\n{y}',
			map(
				lambda g : f'{self.name}({g}) = {self(g)}',
				self.dom
			)
		)
