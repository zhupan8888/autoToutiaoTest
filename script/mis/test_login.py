from page.mis.login_page import LoginProxy
from utils import DriverUtils, element_is_exist
import pytest


@pytest.mark.run(order=102)
class TestLogin:

    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.login_page = LoginProxy()

    def teardown_class(self):
        DriverUtils.quit_mis_driver()

    def test_login(self):
        self.login_page.test_mis_login("testid", "testpwd123")
        is_suc = element_is_exist(self.driver, "1", "管理员")
        assert is_suc
