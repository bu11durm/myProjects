from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('../venv/chromedriver.exe')
driver.get("https://www.baseball-reference.com")
driver.set_window_size(700, 1000)

search = driver.find_element_by_class_name("ac-input.completely")
search.send_keys("Joe Morgan")
search.send_keys(Keys.RETURN)

joes = driver.find_elements_by_class_name("search-item-name")

for joe in joes:
    thetext = joe.find_element_by_css_selector('a').get_attribute('text')
    if '1963' in thetext:
        a_element = joe.find_element_by_css_selector('a')

print(a_element.text)
print(a_element.get_attribute('href'))
a_element.click()
stats = driver.find_element_by_id('batting_standard.1976')
hrs_in_76 = int(stats.find_element_by_xpath('//*[@id="batting_standard.1976"]/td[11]').text)
#print(hrs_in_76)

action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_xpath('//*[@id="inner_nav"]/ul/li[2]/span')
action.move_to_element(firstLevelMenu).perform()

lists = driver.find_elements_by_class_name('listhead')
for list in lists:
#    print('list text ' + list.text)
    if 'Batting Game Logs' in list.text:
#        print('list tag ' + list.tag_name)
        a_element = list.find_element_by_xpath('// *[ @ id = "inner_nav"] / ul / li[2] / div / ul[2] / li[14] / a')
#        print('element tag ' + a_element.tag_name)
#        print('element href ' + a_element.get_attribute('href'))

# print(a_element[])
a_element.click()

hrs_in_gamelog = int(driver.find_element_by_xpath('//*[@id="batting_gamelogs"]/tfoot/tr/td[15]').text)

if hrs_in_76 == hrs_in_gamelog:
    print('hr values match: ' + str(hrs_in_76))
else:
    print('values do not match: ' + str(hrs_in_76) + ' vs ' + str(hrs_in_gamelog))

driver.close()



