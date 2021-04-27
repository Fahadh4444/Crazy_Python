import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

PATH = "F:\Softwares & Tools\Chrome Webdriver\chromedriver.exe"

driver = webdriver.Chrome(PATH)

url = 'https://eduserver.nitc.ac.in/login/index.php'

driver.get(url)


driver.find_element_by_xpath('//*[@id="username"]').send_keys('username')
driver.find_element_by_xpath(
    '//*[@id="password"]').send_keys('password')
driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/section/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/button').click()

driver.implicitly_wait(10)
time.sleep(3)
driver.find_element_by_partial_link_text('Attendance').click()
time.sleep(2)
driver.implicitly_wait(5)
driver.find_element_by_link_text('Go to activity').click()
driver.implicitly_wait(3)
a = 1
b = 0
list = driver.find_elements_by_link_text('Submit attendance')
if(list != []):
    b = 1

while(a):
    if(b):
        time.sleep(2)
        driver.find_element_by_link_text('Submit attendance').click()
        time.sleep(2)
        driver.implicitly_wait(2)
        driver.find_elements_by_class_name('statusdesc')[0].click()
        driver.find_element_by_name('submitbutton').click()
        time.sleep(2)
        a = 0
    else:
        driver.implicitly_wait(1)
        time.sleep(5)
        driver.find_element_by_link_text('Home').click()
        driver.implicitly_wait(10)
        time.sleep(3)
        driver.find_element_by_partial_link_text('Attendance').click()
        time.sleep(2)
        driver.implicitly_wait(5)
        driver.find_element_by_link_text('Go to activity').click()
        driver.implicitly_wait(3)
        list = driver.find_elements_by_link_text('Submit attendance')
        if(list != []):
            b = 1

driver.close()
