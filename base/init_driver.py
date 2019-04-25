from appium import webdriver

#调用该函数就会返回driver
def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 支持中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # app信息 设置开发者头条的包名和启动名
    desired_caps['appPackage'] = 'io.manong.developerdaily'
    desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.MainActivity'
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)