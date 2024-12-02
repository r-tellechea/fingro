import fingro
import numpy as np

def test_quotient_group():
	C2 = fingro.families.Cyclic(2)
	C8 = fingro.families.Cyclic(8)
	C2xC2 = C2 * C2

	H1 = fingro.Subgroup(C2xC2, sub_index=(0,1))
	H2 = fingro.Subgroup(C8, sub_index=(0,2,4,6))
	H3 = fingro.Subgroup(C8, sub_index=(0,4))
	
	assert C2xC2 / H1 == C2
	assert C8 / H2 == fingro.families.Cyclic(2)
	assert C8 / H3 == fingro.families.Cyclic(4)
