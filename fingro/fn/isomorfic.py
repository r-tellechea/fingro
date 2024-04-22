import fingro

def isomorfic(dom: fingro.Group, cod: fingro.Group) -> bool:
	for isomorfism in fingro.compositions.compose_functions.get_isomorfisms(dom, cod):
		return True
	return False
