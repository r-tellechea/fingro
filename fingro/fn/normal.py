import fingro
import numpy as np

def normal(group: fingro.Group, subgroup: fingro.Subgroup) -> bool:
	
	if not fingro.same_matrix(group, subgroup.group):
		raise ValueError('Not subgroup of the group.')
	
	array_index = np.array(
		tuple(
		map(
			lambda t : (t[0][0], t[1], t[0][1]),
			product(
				zip(range(len(group)), group.element_inverses),
				subgroup.sub_index
			)
		))
	)

	ghg1 = group.matrix[
		group.matrix[
			array_index[:,0], 
			array_index[:,1]
		],
		array_index[:,2] 
	]

	return np.in1d(ghg1, np.array(subgroup.sub_index)).all()
