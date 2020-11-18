from appium import webdriver

from time import sleep

desired_capabilities = {
    "platformName":"Android",
    "platformVersion":"5.1.1",
    "appPackage":"com.baidu.wenku",
    "appActivity":"com.baidu.wenku",
    "deviceName":"127.0.0.1:62001"
}
# 打开app
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities)
sleep(2)
# 点击同意并继续
driver.find_element_by_id("com.baidu.wenku:id/tv_agree").click()
