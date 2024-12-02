import fingro
import numpy as np

def test_direct_group():
	C2 = fingro.families.Cyclic(2)
	C3 = fingro.families.Cyclic(3)
	D2 = fingro.families.Dihedral(2)
	
	C3xC3_manual = fingro.Group(
		matrix=np.array([
			[0,1,2, 3,4,5, 6,7,8],
			[1,2,0, 4,5,3, 7,8,6],
			[2,0,1, 5,3,4, 8,6,7],

			[3,4,5, 6,7,8, 0,1,2],
			[4,5,3, 7,8,6, 1,2,0],
			[5,3,4, 8,6,7, 2,0,1],
			
			[6,7,8, 0,1,2, 3,4,5],
			[7,8,6, 1,2,0, 4,5,3],
			[8,6,7, 2,0,1, 5,3,4]
		]),
	)

	assert fingro.compositions.DirectProduct(C2, C2) == D2
	assert fingro.compositions.DirectProduct(C3, C3) == C3xC3_manual
