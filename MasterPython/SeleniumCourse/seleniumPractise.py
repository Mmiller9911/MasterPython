from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

product_list = []
basket_items = []

driver = webdriver.Chrome(executable_path='C:\\seleniumdrivers\chromedriver.exe')
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
driver.find_element_by_css_selector('input.search-keyword').send_keys('ber')
time.sleep(4)
#  driver.find_element_by_css_selector('div.product').send_keys('ber')
number_items = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(number_items)
assert number_items == 3
#  driver.close()

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    product_list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))

basket = driver.find_elements_by_css_selector('p.product-name')
for item in basket:
    basket_items.append(item.text)

print(basket_items)
assert product_list == basket_items

price_before_discount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_css_selector(".promoCode").send_keys('rahulshettyacademy')
driver.find_element_by_css_selector(".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element_by_css_selector(".promoInfo").text)
print(product_list)
price_after_discount = driver.find_element_by_css_selector(".discountAmt").text
print('price before discount is: {},\nprice after discount is: {}'.format(price_before_discount, price_after_discount))
assert float(price_before_discount) > float(price_after_discount)

sum = 0
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
for amount in amounts:
    sum += int(amount.text)

print(sum)
assert int(driver.find_element_by_css_selector(".totAmt").text) == sum
driver.close()
