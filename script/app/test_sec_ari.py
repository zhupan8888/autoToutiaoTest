from page.app.index_page import IndexProxy
from utils import DriverUtils, element_is_exist
import pytest


@pytest.mark.run(order=202)
class TestSecAri:

    def setup_class(self):
        self.driver = DriverUtils.get_app_driver()
        self.index_proxy = IndexProxy()

    def teardown_class(self):
        DriverUtils.quit_app_driver()

    def test_sec_ari(self):
        self.index_proxy.test_sec_aritcal_by_channel("数据库")
        is_suc = element_is_exist(self.driver, "2", "猜你喜欢")
        assert is_suc
