import os
from awesomepy import amath

# fixtures is used to store files used for the tests only
fixtures_loc = os.path.join(os.path.dirname(__file__), 'fixtures')


def test_asum():
    asum_result = amath.asum(1, 1)
    exp_result = 2
    assert asum_result == exp_result
