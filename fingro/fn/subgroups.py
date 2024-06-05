import fingro

def subgroup_eq(subgroup_i: fingro.Subgroup, subgroup_j: fingro.Subgroup) -> bool:
	return set(subgroup_i.sub_index) == set(subgroup_j.sub_index)

def subgroups(group: fingro.Group) -> list[fingro.Subgroup]:	

	if len(group) == 1:
		return [fingro.Subgroup(group, sub_index=(0,))]

	list_subgroups = []
	last_subgroups = []
	
	for i in range(1, len(group)):
		subgroup = fingro.generated_subgroup(group, (i,))
		included = any(
			subgroup_eq(subgroup, subgroup_j) 
				for subgroup_j in last_subgroups
		)
		if not included:
			last_subgroups.append(subgroup)

	while len(last_subgroups) != 0:	
		extended_subgroups = []
		
		for subgroup in last_subgroups:
			
			set_complementary = (
				  set(range(len(group))) 
				- set(subgroup.sub_index)
			)
			discarded = set()
			
			for i in set_complementary:
				if i in discarded:
					continue	
				
				extended_subgroup = fingro.fn.generated_subgroup(
					group, 
					index=(subgroup.sub_index + (i,))
				)
				previous_subgroups = list_subgroups + last_subgroups + extended_subgroups
				
				already_computed = any(
					subgroup_eq(extended_subgroup, subgroup_j) 
						for subgroup_j in previous_subgroups
				)
				if not already_computed:
					extended_subgroups.append(extended_subgroup)
				else:
					discarded = (
						discarded |
						(
							set_complementary 
							- set(extended_subgroup.sub_index)
						)
					)

		list_subgroups += last_subgroups
		last_subgroups = extended_subgroups

	return [fingro.Subgroup(group, sub_index=(0,))] + list_subgroups
