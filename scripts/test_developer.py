import sys,os
sys.path.append(os.getcwd())
from base.read_yaml import read_yaml_data
import pytest
from base.init_driver import  init_driver
from page.home_page import HomePage
from page.my_page import MyPage
from page.login_page import LoginPage
from page.email_login_page import EmailLoginPage
from page.profession_project_page import PrefessionPage
from page.setting_page import SettingPage


# 获取yaml的数据 封装[(1, 2)]格式

def get_test_login_data():
    data_list = []
    login_data = read_yaml_data("login_data.yaml")
    print(login_data)
    for i in login_data.keys():
        username = login_data.get(i).get("username")
        password = login_data.get(i).get("password")
        data_list.append((username, password))
    print(data_list)
    return data_list
class TestDeveloper:
    #保证在test_developer函数执行之前运行 获取self.driver
    def setup_class(self):
        #1.初始化driver
        self.driver = init_driver()
        self.homePage = HomePage(self.driver)
        self.myPage = MyPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.emailLoginPage = EmailLoginPage(self.driver)
        self.professionPage = PrefessionPage(self.driver)
        self.settingPage = SettingPage(self.driver)

    #测试逻辑写到这个函数里面
    @pytest.mark.parametrize("username,password",get_test_login_data())
    def test_developer(self,username,password):
        # 1.点击我的
        self.homePage.test_click_my()
        # 2 点击登录注册
        self.myPage.click_login_regist_btn()
        #3.选择邮箱登录
        self.loginPage.click_email_login()
        #4.输入邮箱密码登录
        self.emailLoginPage.login(username,password)
        #5.点击职业规划
        self.myPage.click_profession_project()
        #6.更新个人信息
        self.professionPage.update_person_info()
        #7.滚动到setting选项
        self.myPage.swip_setting()
        #8.退出账户
        self.settingPage.exit_account()
        #9.验证是否退出成功
        self.myPage.test_verify_logou_sucess()

     #在test_developer运行之后运行
    def teardown_class(self):
        self.driver.quit()


