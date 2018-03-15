import pytest

def inc(x):
    return x + 1

@pytest.mark.xfail #this is expected to fail
def test_answer():
    assert inc(3) == 5 #test that condition and trigger an error if the condition is false