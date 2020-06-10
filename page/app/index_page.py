from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.app.base_page import BasePage, BaseHandle
from utils import DriverUtils


class IndexPage(BasePage):

    def __init__(self):
        super().__init__()
        # 区域
        self.channel_area = (By.CLASS_NAME, "android.widget.HorizontalScrollView")
        # 指定频道
        self.channel_option = (By.XPATH, "//*[contains(@text,'{}')]")
        # 查看一组文章
        self.aritcal_option = (By.XPATH, "//*[contains(@text,'评论')]")

    def find_channel_area(self):
        return self.find_elt(self.channel_area)

    def find_channel_option(self, channel):
        return self.driver.find_element(self.channel_option[0], self.channel_option[1].format(channel))

    def find_aritcal_option(self):
        return self.find_elt(self.aritcal_option)


class IndexHandle(BaseHandle):

    def __init__(self):
        self.index_page = IndexPage()
        self.driver = DriverUtils.get_app_driver()

    def check_channel(self, channel):
        area = self.index_page.find_channel_area()
        x = area.location["x"]
        y = area.location["y"]

        w = area.size["width"]
        h = area.size["height"]

        start_x = x + w * 0.75
        start_y = y + y * 0.5

        end_x = x + w * 0.25
        end_y = start_y

        while True:
            page_start = self.driver.page_source
            try:
                self.index_page.find_channel_option(channel).click()
                break
            except Exception as e:
                self.driver.swipe(start_x, start_y, end_x, end_y)

            if page_start == self.driver.page_source:
                print("No such {} channel".format(channel))
                raise NoSuchElementException

    def click_aritcal_option(self):
        self.index_page.find_aritcal_option().click()


class IndexProxy:

    def __init__(self):
        self.index_handle = IndexHandle()

    def test_sec_aritcal_by_channel(self, channel):
        self.index_handle.check_channel(channel)
        self.index_handle.click_aritcal_option()
