from selenium import webdriver

driver = webdriver.Chrome('../venv/chromedriver.exe')
driver.get('https://www.espn.com/fantasy/hockey/story/_/id/29458089/end-season-rankings-keep-draft-next-season')
ranks = driver.find_elements_by_class_name('last')
print('{')
for rank in ranks:
    first_split = rank.get_attribute('innerHTML').split('<td>')
    second_split = first_split[1].split('.',1)
    if "a href" in second_split[1]:
        third_split = second_split[1].split('">')
        fourth_split = third_split[1].split('</a>')
        player_name = fourth_split[0]
    else:
        third_split = second_split[1].split(',')
        player_name = third_split[0].strip()
    print('    "' + player_name + '" : "'+ second_split[0] + '",')
print('}')