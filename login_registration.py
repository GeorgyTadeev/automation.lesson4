#Registration_login: регистрация аккаунта
'''import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
btn_menu = driver.find_element_by_css_selector("#menu-item-50 a")
btn_menu.click()
inp_reg_email = driver.find_element_by_id("reg_email")
inp_reg_email.send_keys("tester2022@test.com")
inp_reg_password = driver.find_element_by_id("reg_password")
time.sleep(1)
inp_reg_password.send_keys("Test123Pass!")
btn_register = driver.find_element_by_name("register")
btn_register.click()
driver.quit()'''

#Registration_login: логин в систему
'''from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
btn_menu = driver.find_element_by_css_selector("#menu-item-50 a")
btn_menu.click()
inp_login = driver.find_element_by_id("username")
inp_login.send_keys("tester2022@test.com")
inp_password = driver.find_element_by_id("password")
inp_password.send_keys("Test123Pass!")
btn_register = driver.find_element_by_name("login")
btn_register.click()
btn_logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link--customer-logout a")
btn_logout_text = btn_logout.text
assert "Logout" in btn_logout_text
driver.quit()'''