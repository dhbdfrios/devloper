from base.base_action import BaseAction
class PrefessionPage(BaseAction):
    def __init__(self,driver):
        # self.driver = driver
        BaseAction.__init__(self,driver)

    def update_person_info(self):
        #更新工作年限
        self.driver.find_element_by_id("io.manong.developerdaily:id/tv_working_years").click()
        first_ele = self.driver.find_element_by_xpath("//*[contains(@text,'应届毕业生')]").location
        five_ele = self.driver.find_element_by_xpath("//*[contains(@text,'5年')]").location
        self.driver.swipe(five_ele["x"], five_ele["y"], first_ele["x"], first_ele["y"], 2000)
        self.driver.find_element_by_xpath("//*[contains(@text,'10年以上')]").click()

        #职位类型
        self.driver.find_element_by_id("io.manong.developerdaily:id/tv_expect_job_type").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'测试')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动端测试')]").click()

        #修改期望城市(选择其他)
        self.driver.find_element_by_id("io.manong.developerdaily:id/tv_expect_city").click()
        wuhan_ele = self.driver.find_element_by_xpath("//*[contains(@text,'武汉')]")
        shanghai_ele = self.driver.find_element_by_xpath("//*[contains(@text,'上海')]")
        self.driver.drag_and_drop(wuhan_ele, shanghai_ele)
        self.driver.find_element_by_xpath("//*[contains(@text,'其他')]").click()
        except_city = self.driver.find_element_by_class_name("android.widget.EditText")
        except_city.clear()
        except_city.send_keys("东京")
        self.driver.find_element_by_id("io.manong.developerdaily:id/md_buttonDefaultPositive").click()

        #修改当前状态
        self.driver.find_element_by_id("io.manong.developerdaily:id/tv_current_status").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'暂时不换')]").click()

        # 点击保存
        self.driver.find_element_by_id("io.manong.developerdaily:id/action_save").click()