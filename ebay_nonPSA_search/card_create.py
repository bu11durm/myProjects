
from found_card import Found_card

def create_card(headline, item2):
    next_divs = item2.find_all('div')
    detail_div = next_divs[0].find_next_sibling('div')
    image_div = next_divs[1]
    thumbnail = image_div.find_next('img')
    link = detail_div.find_next('a')
    found_card = Found_card(headline, link['href'], thumbnail['src'],detail_div.find_next('span', attrs={'s-item__bids s-item__bidCount'}).string, detail_div.find_next('span', attrs={'s-item__price'}).string)
    return found_card