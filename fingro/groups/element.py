from dataclasses import dataclass

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
