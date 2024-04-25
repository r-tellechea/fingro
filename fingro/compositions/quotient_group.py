import fingro
import numpy as np

def quotient_matrix_classes_names(group: fingro.Group, subgroup: fingro.Subgroup):
		
	array_classes = (
		np.unique(
			np.sort(
				group.matrix[:,subgroup.sub_index],
				axis=1
			),
			axis=0
		)
	)
	array_class_representatives = array_classes.min(axis=1)

	sub_matrix = (
		group.matrix
		[array_class_representatives,:]
		[:,array_class_representatives]
	)

	# TODO: There is probably a better way to do this.
	array_class_index = np.zeros((len(group),))
	for array_index, class_element in enumerate(array_classes.ravel()):
		class_index = array_index // len(subgroup)
		array_class_index[class_element] = class_index
	
	matrix = (
		array_class_index
		[sub_matrix.ravel()]
		.reshape(sub_matrix.shape)
		.astype('int')
	)

	return (
		# Matrix
		matrix,
		
		# Classes.
		tuple(
			tuple(class_array)
				for class_array in array_classes
		),

		# Class names.
		tuple(
			f'[{group.element_names[i]}]' 
				for i in array_class_representatives
		)
	)


class QuotientGroup(fingro.Group):
	def __init__(self, group: fingro.Group, subgroup: fingro.Subgroup):
		if not fingro.is_subgroup(subgroup, group):
			raise ValueError('Not a subgroup of the group')
		if not subgroup.normal:
			raise ValueError('Not a normal subgroup.')
		
		matrix, classes, names = quotient_matrix_classes_names(
			group, subgroup
		)
		
		super().__init__(
			matrix=matrix,
			name=f'{group.name}/{subgroup.name}',
			elements=classes,
			element_names=quotient_names(group, subgroup),
			check_matrix_type_and_shape=False,
			check_group_properties=False
		)
