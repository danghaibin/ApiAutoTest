from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

try:
    driver = webdriver.Chrome()

    driver.get("https://www.baidu.com")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # 获取窗口的尺寸
    size = driver.get_window_size()
    print("窗口的尺寸%s"%size)

    # 点击百度
    # search = driver.find_element_by_id('kw')
    # # driver.find_element_by_id('su').click()
    # search.send_keys('西安')
    # 键盘操作
    # search.send_keys(Keys.ENTER)
    # 鼠标操作
    driver.find_element_by_id('kw').send_keys('西安')
    btn = driver.find_element_by_id('su')
    ActionChains(driver).click(btn).perform()
except Exception as e:
    print(e)

finally:
    sleep(200)
    driver.close()


