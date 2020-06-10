from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle


class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        self.info_manage = (By.XPATH, "//*[text()='信息管理']")
        self.aduit_manage = (By.XPATH, "//*[text()='内容审核']")

    def find_info_manage(self):
        return self.find_elt(self.info_manage)

    def find_aduit_manage(self):
        return self.find_elt(self.aduit_manage)

class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    def click_info_manage(self):
        self.home_page.find_info_manage().click()

    def click_aduit_manage(self):
        self.home_page.find_aduit_manage().click()

class HomePorxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    def to_aduit_aritcal(self):
        self.home_handle.click_info_manage()
        self.home_handle.click_aduit_manage()
