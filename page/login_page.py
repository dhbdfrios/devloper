from base.base_action import BaseAction
import base
class LoginPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self, driver)

    #选择邮箱登录
    def click_email_login(self):
        # self.driver.find_element_by_id("io.manong.developerdaily:id/btn_email").click()
        self.click_element(base.login_page_btn_email_login)