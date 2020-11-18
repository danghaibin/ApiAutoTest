from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()
    driver.implicitly_wait(10)

    # search = driver.find_element_by_name('wd')
    # search.send_keys('中国富平')
    # search.send_keys(Keys.ENTER)

    driver.find_element_by_name("wd").send_keys('中国富平')
    btn = driver.find_element_by_id('su')
    ActionChains(driver).click(btn).perform()


except Exception as e:
    print(e)

finally:
    sleep(200)
    driver.close()