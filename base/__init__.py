from selenium.webdriver.common.by import By

#1 email_login_page
email_login_page_edit_email = By.ID,"io.manong.developerdaily:id/edt_email"
email_login_page_edit_pwd = By.ID,"io.manong.developerdaily:id/edt_password"
email_login_page_btn_login = By.ID,"io.manong.developerdaily:id/btn_login"


#2 home_page
home_page_btn_my = By.XPATH,"//*[contains(@text,'我的')]"

#3 login_page
login_page_btn_email_login = By.ID,"io.manong.developerdaily:id/btn_email"

#4 my_page
my_page_btn_login_register = By.ID,"io.manong.developerdaily:id/login_btn"
my_page_btn_profession_project = By.ID,"io.manong.developerdaily:id/nav_btn_ucp"

my_page_text_my_icon = By.XPATH,"//*[contains(@text,'我的IO币')]"
my_page_text_nick_name = By.XPATH,"//*[contains(@text,'xiha23')]"

my_page_btn_login = By.ID,"io.manong.developerdaily:id/login_btn"
my_page_btn_my_icon = By.ID,"io.manong.developerdaily:id/nav_btn_coin_total"
my_page_btn_setting = By.ID,"io.manong.developerdaily:id/nav_btn_setting"
my_page_text_login = By.ID,"io.manong.developerdaily:id/login_btn"

#5 profession_project
profession_project_page_btn_work_years =By.ID,"io.manong.developerdaily:id/tv_working_years"
profession_project_page_work_years_swip1 =By.XPATH,"//*[contains(@text,'应届毕业生')]"
profession_project_page_work_years_swip2 =By.XPATH,"//*[contains(@text,'5年')]"
profession_project_page_btn_ten_years =By.XPATH,"//*[contains(@text,'10年以上')]"
#...

#6 setting_page
setting_page_btn_logout = By.ID,"io.manong.developerdaily:id/btn_logout"
setting_page_btn_Positive = By.ID,"io.manong.developerdaily:id/md_buttonDefaultPositive"





