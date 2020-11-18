from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.maximize_window()
    sleep(5)

    driver.find_element_by_id('kw').send_keys('python')

    sleep(2)
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys('Java')
    driver.find_element_by_id('su').click()
    sleep(5)
    # 点击
    driver.find_elements_by_link_text('百度百科').click()
    handles = driver.window_handles
    driver.switch_to_window(handles[1])
    sleep(3)
    # driver.

except Exception as e:
    print(e)
finally:
    sleep(100)
    driver.close()
