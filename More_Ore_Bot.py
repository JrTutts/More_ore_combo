import imp
from operator import truediv
from selenium import webdriver
import time
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/path/to/my/profile')
driver = webdriver.Chrome(PATH, chrome_options=options)


driver.get("https://syns.studio/more-ore/")
print(driver.title)


# Sleep timer is so you can click through menus and properly load the game before the clicker starts running
time.sleep(5)


while True:
    try:
        elem = driver.find_element_by_class_name('weak-spot')
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(
            elem, random.randint(0, 20), random.randint(0, 20))
        action.click()
        action.perform()

        time.sleep(random.uniform(0.273, 0.65))
    except:
        print("WEAK SPOT NOT FOUND")
        time.sleep(1)
