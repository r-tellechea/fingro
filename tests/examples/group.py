import pytest
from tests.examples.families.dihedrals import D4

@pytest.fixture
def group(D4):
	return D4
