
import pytest


@pytest.mark.smoke
def test_first_program(setup):
    print("hello")


@pytest.mark.xfail
def test_CreditCard4(setup):
    print("do not add me to the report")


def test_crossBrowser(crossbrowser):  # call the crossbrowser fixture
    print(crossbrowser[0])
   # print(crossbrowser)




