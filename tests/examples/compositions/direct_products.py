import fingro
import pytest

from tests.examples.families.cyclics import C2, C3

@pytest.fixture
def C2xC2(C2):
	return fingro.compositions.direct_product.DirectProduct(C2, C2)

@pytest.fixture
def C3xC3(C3):
	return fingro.compositions.direct_product.DirectProduct(C3, C3)
