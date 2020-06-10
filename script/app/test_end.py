from utils import DriverUtils
import pytest


# 装饰器指定测试用例文件执行的顺序
@pytest.mark.run(order=299)
class TestEnd:

    def test_end(self):
        # 关闭 关闭浏览器驱动的开关
        DriverUtils.change_app_key(True)
        DriverUtils.quit_app_driver()
