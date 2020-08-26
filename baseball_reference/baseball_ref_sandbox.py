from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

# adding comment for github test
driver = webdriver.Chrome('../venv/chromedriver.exe')
driver.get("https://www.baseball-reference.com/players/m/morgajo02.shtml")
driver.set_window_size(700, 1000)

action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_xpath('//*[@id="inner_nav"]/ul/li[2]/span')
action.move_to_element(firstLevelMenu).perform()

driver.close