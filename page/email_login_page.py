from base.base_action import BaseAction
import base
class EmailLoginPage(BaseAction):
    def __init__(self,driver):
        # self.driver = driver
        BaseAction.__init__(self,driver)
    # 实现输入用户名和密码 点击登录完成
    def login(self,username,password):
        self.input_edit_content(base.email_login_page_edit_email,username)
        self.input_edit_content(base.email_login_page_edit_pwd,password)
        self.click_element(base.email_login_page_btn_login)
	print("aaa")
