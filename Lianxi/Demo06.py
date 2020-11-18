from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

try:

    # 获取url
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/')
    driver.maximize_window()
    driver.implicitly_wait(10)

    #登录
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()

    # 进入后台管理
    driver.find_element_by_id('s-menu-superadmin').click()

    # 进入iframe
    iframe = driver.find_element_by_id('iframe-superadmin')
    driver.switch_to.frame(iframe)

    # 添加成员
    driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]').click()

    # 添加成员信息
    driver.find_element_by_id('account').send_keys('qwerq2')
    driver.find_element_by_id('realname').send_keys('asd')
    driver.find_element_by_id('genderm').click()

    # 部门
    dept = driver.find_element_by_id('dept').click()
    depts = Select(dept)
    depts.deselect_by_value('9')

    # 角色
    role = driver.find_element_by_id('role').click()
    roles = Select(role)
    roles.select_by_visible_text('项目经理')

except Exception as e:
    print(e)

finally:
    sleep(500)
    driver.quit()
