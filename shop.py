#Shop: отображение страницы товара
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
btn_shop = driver.find_element_by_css_selector("#menu-item-40 a")
btn_shop.click()
btn_html5 = driver.find_element_by_css_selector(".post-181 a")
btn_html5.click()
tlt_book = driver.find_element_by_class_name("product_title.entry-title")
tlt_book_text = tlt_book.text
assert "HTML5 Forms" in tlt_book_text
driver.quit()'''

#Shop: количество товаров в категории
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
btn_shop = driver.find_element_by_css_selector("#menu-item-40 a")
btn_shop.click()
btn_html = driver.find_element_by_css_selector(".cat-item-19 a")
btn_html.click()
cnt_product = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
assert len(cnt_product) == 3
driver.quit()'''

#Shop: сортировка товаров
'''from selenium import webdriver
from selenium.webdriver.support.select import Select
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
btn_shop = driver.find_element_by_css_selector("#menu-item-40 a")
btn_shop.click()
skt_sorting = driver.find_element_by_class_name("orderby")
skt_sorting_value = skt_sorting.get_attribute("value")
assert skt_sorting_value == "menu_order"
select = Select(skt_sorting)
select.select_by_value("price-desc")
skt_sorting = driver.find_element_by_class_name("orderby")
skt_sorting_value = skt_sorting.get_attribute("value")
assert skt_sorting_value == "price-desc"
driver.quit()'''

#Shop: отображение, скидка товара
'''from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
btn_shop = driver.find_element_by_css_selector("#menu-item-40 a")
btn_shop.click()
btn_android_qsg = driver.find_element_by_css_selector(".post-169 a")
btn_android_qsg.click()
txt_old_price = driver.find_element_by_css_selector(".price > del > span")
txt_old_price_text = txt_old_price.text
assert txt_old_price_text == "₹600.00"
txt_new_price = driver.find_element_by_css_selector(".price > ins > span")
txt_new_price_text = txt_new_price.text
assert txt_new_price_text == "₹450.00"
btn_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images a")))
btn_cover.click()
btn_close_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
btn_close_cover.click()
driver.quit()'''

#Shop: проверка цены в корзине
'''import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
btn_shop = driver.find_element_by_css_selector("#menu-item-40 a")
btn_shop.click()
btn_add_html5 = driver.find_element_by_css_selector(".post-182 > .button")
btn_add_html5.click()
time.sleep(1)
txt_cart_item = driver.find_element_by_class_name("cartcontents")
txt_cart_item_text = txt_cart_item.text
assert txt_cart_item_text == "1 Item"
txt_cart_price = driver.find_element_by_class_name("wpmenucart-contents .amount")
txt_cart_price_text = txt_cart_price.text
assert txt_cart_price_text == "₹180.00"
btn_cart = driver.find_element_by_class_name("wpmenucart-contents")
btn_cart.click()
txt_subtotal_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal .amount"), "₹180.00"))
txt_total_text = WebDriverWait(driver, 10).until_not(
    EC.invisibility_of_element_located((By.CLASS_NAME, "order-total .amount")))
driver.quit()'''

#Shop: работа в корзине
'''import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
btn_shop = driver.find_element_by_css_selector("#menu-item-40 a")
btn_shop.click()
driver.execute_script("window.scrollBy(0, 300);")
btn_add_html5 = driver.find_element_by_class_name("post-182 .button")
btn_add_html5.click()
time.sleep(1)
btn_add_html5 = driver.find_element_by_class_name("post-180 .button")
btn_add_html5.click()
time.sleep(1)
btn_cart = driver.find_element_by_class_name("wpmenucart-contents")
btn_cart.click()
time.sleep(1)
btn_delete_first_book = driver.find_element_by_css_selector(".cart_item:nth-child(1) .product-remove a")
btn_delete_first_book.click()
btn_undo = driver.find_element_by_css_selector(".woocommerce-message a")
btn_undo.click()
inp_count_first_book = driver.find_element_by_class_name("cart_item:nth-child(1) .input-text")
inp_count_first_book.clear()
inp_count_first_book.send_keys("3")
btn_update_basket = driver.find_element_by_css_selector(".actions > .button")
btn_update_basket.click()
inp_count_first_book_value = inp_count_first_book.get_attribute("value")
assert inp_count_first_book_value == "3"
time.sleep(1)
btn_coupon = driver.find_element_by_css_selector(".coupon > .button")
btn_coupon.click()
txt_error = driver.find_element_by_css_selector(".woocommerce-error > li")
txt_error_text = txt_error.text
assert "Please enter a coupon code." == txt_error_text
driver.quit()'''

#Shop: покупка товара
'''import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
btn_shop = driver.find_element_by_css_selector("#menu-item-40 a")
btn_shop.click()
driver.execute_script("window.scrollBy(0, 300);")
btn_add_html5 = driver.find_element_by_class_name("post-182 .button")
btn_add_html5.click()
time.sleep(1)
btn_cart = driver.find_element_by_class_name("wpmenucart-contents")
btn_cart.click()
btn_proceed_to_checkout = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout a")))
btn_proceed_to_checkout.click()
time.sleep(1)
inp_first_name = driver.find_element_by_id("billing_first_name")
inp_first_name.send_keys("TesterFN")
inp_last_name = driver.find_element_by_id("billing_last_name")
inp_last_name.send_keys("TesterLN")
inp_email = driver.find_element_by_id("billing_email")
inp_email.send_keys("tester2022@test.com")
inp_phone = driver.find_element_by_id("billing_phone")
inp_phone.send_keys("+79681049484")
sel_open = driver.find_element_by_id("select2-chosen-1")
sel_open.click()
inp_country = driver.find_element_by_id("s2id_autogen1_search")
inp_country.send_keys("Russia")
btn_country = driver.find_element_by_class_name("select2-match")
btn_country.click()
inp_adr = driver.find_element_by_id("billing_address_1")
inp_adr.send_keys("Lenin street, 24")
inp_city = driver.find_element_by_id("billing_city")
inp_city.send_keys("Omsk")
inp_state = driver.find_element_by_id("billing_state")
inp_state.send_keys("Region 55")
inp_postcode = driver.find_element_by_id("billing_postcode")
inp_postcode.send_keys("644041")
cbx_check_payments = driver.find_element_by_id("payment_method_cheque")
cbx_check_payments.click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
btn_place_order = driver.find_element_by_id("place_order")
btn_place_order.click()
txt_thank_you = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
txt_check_payments = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method > strong"), "Check Payments"))
driver.quit()'''