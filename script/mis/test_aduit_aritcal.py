from config import BASE_ARITCAL_TITLE
from page.mis.aduit_page import AduitProxy
from page.mis.home_page import HomePorxy
from utils import DriverUtils, element_is_exist

import pytest


@pytest.mark.run(order=103)
class TestAdAritcal:

    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.home_proxy = HomePorxy()
        self.ad_proxy = AduitProxy()

    def teardown_class(self):
        DriverUtils.quit_mis_driver()

    def test_aduit_aritcal(self):
        self.home_proxy.to_aduit_aritcal()
        self.ad_proxy.test_aduit_aritcal("TestCase")
        is_suc = element_is_exist(self.driver,"1","TestCase")
        assert is_suc
