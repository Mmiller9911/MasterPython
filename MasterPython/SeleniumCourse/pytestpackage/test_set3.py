
import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo(self):
        print("test_fixture_demo")

    def test_fixture_demo1(self):
        print("test_fixture_demo_1")

    def test_fixture_demo2(self):
        print("test_fixture_demo_2")

    def test_fixture_demo3(self):
        print("test_fixture_demo_3")