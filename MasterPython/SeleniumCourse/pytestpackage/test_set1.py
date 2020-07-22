import pytest

@pytest.mark.skip
def test_CreditCard1(setup):
    msg = 'hello'
    assert msg == 'Hi', "Test has failed, sigh"


def test_CreditCard2(setup):
    print("goodbye")


@pytest.mark.smoke
def test_CreditCard3(setup):
    print("goodbye")

