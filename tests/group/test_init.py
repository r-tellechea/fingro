import pytest
import fingro

import numpy as np

@pytest.mark.skip
def test_check_matrix_shape():
	try:
		fingro.Group(
			matrix=np.array([
				[0,1,2], 
				[1,2,3]
			]),
			check_matrix_type_and_shape=True
		)
		assert False
	except ValueError as e:
		assert str(e) == 'Wrong matrix shape.'

def test_check_neutral_element():
	try:
		fingro.Group(
			matrix=np.array([
				[0,1,2,3],
				[1,2,3,0],
				[3,3,0,1],
				[3,0,1,2],
			]),
			check_group_properties=True
		)
		assert False
	except ValueError as e:
		assert str(e) == 'Property: Neutral element.'

def test_check_inverse_element():
	try:
		fingro.Group(
			matrix=np.array([
				[0,1],
				[1,1],
			]),
			check_group_properties=True
		)
		assert False
	except ValueError as e:
		assert str(e) == 'Property: Inverse element.'

def test_check_associativity():
	try:
		fingro.Group(
			matrix=np.array([
				[0,1,2],
				[1,0,2],
				[2,2,0],
			]),
			check_group_properties=True
		)
		assert False
	except ValueError as e:
		assert str(e) == 'Property: Associativity.'
