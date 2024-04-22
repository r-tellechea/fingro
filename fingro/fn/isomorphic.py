import fingro

def isomorphic(dom: fingro.Group, cod: fingro.Group) -> bool:
	for isomorphism in fingro.compositions.compose_functions.get_isomorphisms(dom, cod):
		return True
	return False
