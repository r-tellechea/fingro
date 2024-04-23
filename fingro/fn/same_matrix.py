import fingro
import numpy as np

def same_matrix(G: fingro.Group, H: fingro.Group) -> bool:
	return np.array_equal(G.matrix, H.matrix)
