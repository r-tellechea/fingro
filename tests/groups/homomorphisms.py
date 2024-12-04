import fingro
import pytest

import numpy as np

from tests.groups.cyclics import C2, C4

@pytest.fixture
def inclusion_C2_C4(C2, C4):
	return fingro.Homomorphism(
		f=(np.arange(2) * 2),
		dom=C2,
		cod=C4,
		check_homomorphism=False
	)

@pytest.fixture
def projection_C4_C2(C2, C4):
	return fingro.Homomorphism(
		f=(np.arange(4) % 2),
		dom=C4,
		cod=C2,
		check_homomorphism=False
	)

@pytest.fixture
def isomorphism_C4(C4):
	return fingro.Homomorphism(
		f=np.arange(4),
		dom=C4,
		cod=C4,
		check_homomorphism=False
	)

@pytest.fixture
def isomorphism_not_trivial_C4(C4):
	return fingro.Homomorphism(
		f=np.array([0, 3, 2, 1]),
		dom=C4,
		cod=C4,
		check_homomorphism=False
	)

@pytest.fixture
def endomorphism_subgroup_C4(C4):
	return fingro.Homomorphism(
		f=((np.arange(4) * 2) % 4),
		dom=C4,
		cod=C4,
		check_homomorphism=False
	)
