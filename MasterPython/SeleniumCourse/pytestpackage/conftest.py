import pytest


@pytest.fixture(scope='class')
def setup():
    print("SETUP")  # setup browser etc
    yield
    print("TEARDOWN")  # kill all the cookies etc


@pytest.fixture()
def dataLoad():
    print("profile data being created")
    return ["Matthew", "Miller", "Mils.com"]


@pytest.fixture(params=[("chrome", "Matt", "Miller"), ("Firefox", "Data"), ("Justone")])  # each time the test runs the param(s) will be sent to the function "request" object
def crossbrowser(request):
    return request.param  # request is part of the fixture object

