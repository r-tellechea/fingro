import fingro

def test_mul():
	C3 = fingro.families.Cyclic(3)
	assert C3 * C3 == fingro.compositions.DirectProduct(C3, C3)

def test_xor():
	C3 = fingro.families.Cyclic(3)
	assert C3 ^ C3 == fingro.compositions.HomomorphismsGroup(C3, C3)
