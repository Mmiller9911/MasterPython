import pytest

from SeleniumCourse.pytestpackage.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editprofile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad)
        print(dataLoad[2])


