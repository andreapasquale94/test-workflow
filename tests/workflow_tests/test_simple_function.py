from src.workflow.simple_function import addition, stack

import numpy as np


def test_addition():
    assert 4 == addition(2, 2)


def test_stack():
    assert np.array([2, 2]) == stack(2, 2)