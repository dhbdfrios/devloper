from base.base_action import BaseAction
import base
class HomePage(BaseAction):
    def __init__(self,driver):
        # self.driver = driver
        BaseAction.__init__(self,driver)
    #点击我的
    def test_click_my(self):
        self.click_element(base.home_page_btn_my)
