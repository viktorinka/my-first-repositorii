from selenium import webdriver
import math
import time 
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome() 
browser.get(link)
x_element = browser.find_element_by_xpath("//div //span[@class='nowrap']//@id")
x = x_element.text
y = calc(x)
input1 = browser.find_element_by_id("answer")
input1.send_keys("y")
option1 = browser.find_element_by_css_selector("//input[@class='form-check-input'] //@required")
option1.click()
option2 = browser.find_element_by_css_selector("//input[@class='form-check-input'] [@value='robots']")
option2.click()
button = browser.find_element_by_css_selector("btn btn-default") 
button.click()
# успеваем скопировать код за 30 секунд 
time.sleep(30) 
# закрываем браузер после всех манипуляций 
browser.quit()
# пустая строка для линукса, а то окно не закроет
