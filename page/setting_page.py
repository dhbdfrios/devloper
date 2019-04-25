from base.base_action import BaseAction
import base
class SettingPage(BaseAction):
    def __init__(self,driver):
        # self.driver = driver
        BaseAction.__init__(self,driver)

    #点击退出账号
    def exit_account(self):
        self.click_element(base.setting_page_btn_logout)
        self.click_element(base.setting_page_btn_Positive)

        # self.driver.find_element_by_id("io.manong.developerdaily:id/btn_logout").click()
        # self.driver.find_element_by_id("io.manong.developerdaily:id/md_buttonDefaultPositive").click()