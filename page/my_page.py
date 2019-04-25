from base.base_action import BaseAction
import base

class MyPage(BaseAction):
    def __init__(self,driver):
        # self.driver = driver
        BaseAction.__init__(self,driver)
    #点击登录注册按钮
    def click_login_regist_btn(self):
        self.click_element(base.my_page_btn_login_register)

    #点击职业规划
    def click_profession_project(self):
        self.click_element(base.my_page_btn_profession_project)


    #实现滑动到设置
    def swip_setting(self):
        # my_icon = self.driver.find_element_by_xpath("//*[contains(@text,'我的IO币')]").location
        # nick_name = self.driver.find_element_by_xpath("//*[contains(@text,'xiha23')]").location

        my_icon = self.find_element(base.my_page_text_my_icon).location
        nick_name = self.find_element(base.my_page_text_nick_name).location
        self.driver.swipe(my_icon.get("x"), my_icon.get("y"), nick_name.get("x"), nick_name.get("y"), 2000)
        self.click_element(base.my_page_btn_setting)

        # self.driver.find_element_by_id("io.manong.developerdaily:id/nav_btn_setting").click()

    #校验是否退出成功
    def test_verify_logou_sucess(self):
        # my_icon = self.driver.find_element_by_id("io.manong.developerdaily:id/nav_btn_coin_total")
        # my_setting = self.driver.find_element_by_id("io.manong.developerdaily:id/nav_btn_setting")
        my_icon = self.find_element(base.my_page_btn_my_icon)
        my_setting = self.find_element(base.my_page_btn_setting)
        self.driver.drag_and_drop(my_icon, my_setting)
        # login_info = self.driver.find_element_by_id("io.manong.developerdaily:id/login_btn").text
        login_info = self.find_element(base.my_page_text_login).text
        if "登录" in login_info:
            print("退出成功")
        else:
            print("退出失败")
