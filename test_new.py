import pytest

def inc(x):
    return x + 1

@pytest.mark.xfail
def test_answer():
    assert inc(3) == 8
