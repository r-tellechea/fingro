import fingro

class EndomorfismsGroup(fingro.compositions.HomomorfismsGroup):
	def __init__(self, G: fingro.Group):
		super().__init__(G, G)
