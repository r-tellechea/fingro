import fingro

def isomorphism_gen_im_filter(dom: fingro.Group, cod: fingro.Group) -> dict[int, tuple[int]]:
	return {
		i : tuple(
			j for j in range(len(cod)) 
				if dom.element_orders[i] == cod.element_orders[j]
		)
			for i in dom.generators
	}
