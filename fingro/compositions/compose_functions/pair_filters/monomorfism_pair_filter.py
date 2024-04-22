import fingro

def monomorfism_pair_filter(dom: fingro.Group, cod: fingro.Group) -> dict[int, tuple[int]]:
	return {
		i : tuple(
			j for j in range(min(1, i), len(cod)) 
				if dom.element_orders[i] % cod.element_orders[j] == 0
		)
			for i in range(len(dom))
	}
