import time

from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle
from utils import select_option, DriverUtils


class AduitPage(BasePage):

    def __init__(self):
        super().__init__()
        self.query_btn = (By.CSS_SELECTOR, ".find")
        self.aduit_btn = (By.XPATH, "//*[text()='通过']")
        self.submit_btn = (By.CSS_SELECTOR, ".el-button--primary")
        self.query_box = (By.XPATH, "//*[contains(@placeholder,'请输入: 文章')]")
        self.end_time = (By.CSS_SELECTOR,"[placeholder*='结束']")

    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    def find_aduit_btn(self):
        return self.find_elt(self.aduit_btn)

    def find_submit_btn(self):
        return self.find_elt(self.submit_btn)

    def find_query_box(self):
        return self.find_elt(self.query_box)

    def find_end_time(self):
        return self.find_elt(self.end_time)


class AduitHandle(BaseHandle):

    def __init__(self):
        self.aduit_page = AduitPage()
        self.driver = DriverUtils.get_mis_driver()

    def query_wait_aduit(self, title, status):
        select_option(self.driver, "请选择状态", status)
        self.input_text(self.aduit_page.find_query_box(), title)
        self.aduit_page.find_end_time().clear()
        self.aduit_page.find_query_btn().click()

    def click_aduit_btn(self):
        self.aduit_page.find_aduit_btn().click()

    def click_submit_btn(self):
        self.aduit_page.find_submit_btn().click()


class AduitProxy:
    def __init__(self):
        self.aduit_handle = AduitHandle()
        self.driver = DriverUtils.get_mis_driver()

    def test_aduit_aritcal(self, title):
        self.aduit_handle.query_wait_aduit(title, "待审核")
        time.sleep(5)
        self.aduit_handle.click_aduit_btn()
        time.sleep(2)
        self.aduit_handle.click_submit_btn()
        self.aduit_handle.query_wait_aduit(title, "审核通过")
