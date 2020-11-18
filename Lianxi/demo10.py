from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

try:

    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.maximize_window()
    driver.implicitly_wait(10)

    size = driver.get_window_size()
    print('窗口的大小%s'%size)

    driver.find_element_by_id('su').click()

    driver.find_element_by_id('kw').send_keys('富平县')

    search = driver.find_element_by_id('kw')
    search.send_keys('gff')
    search.send_keys(Keys.ENTER)

    # ActionChains(driver).click(btn).perform()
except Exception as e:
    print(e)

finally:
    sleep(100)
    driver.close()

