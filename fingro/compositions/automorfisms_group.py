import fingro

class AutomorfismsGroup(fingro.compositions.IsomorfismsGroup):
	def __init__(self, G: fingro.Group):
		super().__init__(G, G)
