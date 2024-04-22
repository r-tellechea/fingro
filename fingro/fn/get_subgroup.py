import fingro

def get_subgroup(dom: fingro.Group, cod: fingro.Group) -> fingro.Subgroup | None:
	for monomorfism in fingro.compositions.compose_functions.get_monomorfisms(dom, cod):
		return monomorfism.im()
	return None
