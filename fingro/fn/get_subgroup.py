import fingro

def get_subgroup(dom: fingro.Group, cod: fingro.Group) -> fingro.Subgroup | None:
	for monomorphism in fingro.compositions.compose_functions.get_monomorphisms(dom, cod):
		return monomorphism.im()
	return None
