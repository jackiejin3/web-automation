#encoding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://10.73.4.194:8080/")
driver.maximize_window()
login_handle = driver.current_window_handle
#print(driver.current_url)
#print(driver.page_source)
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_id('password').send_keys('admin123')
driver.find_element_by_id('button').click()

#print(driver.current_url)
#print(driver.page_source)

sleep(5)
driver.switch_to.frame("contentframe")

#tr = WebDriverWait(driver, timeout=5, poll_frequency=0.5).until(EC.presence_of_element_located((By.ID, 'devlistTr_0')))
driver.find_element_by_xpath("//tr[@id='devlistTr_0']/td[2]/input").click()
driver.switch_to.default_content()
alert = driver.find_element_by_css_selector("[class*=aui_state_focus]")
#WebDriverWait(driver, 5, 0.5).until(EC.alert_is_present())
#alert = driver.switch_to.alert()
print(alert.text)
#点击确定
driver.find_element_by_id("artConfirmBut").click()
#点击取消
#driver.find_element_by_id("artCancelBut").click()
#driver.quit()