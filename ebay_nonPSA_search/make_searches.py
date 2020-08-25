import requests
from bs4 import BeautifulSoup

start_year = 1956
end_year = 1979
checklist_url = 'https://www.baseball-almanac.com/baseball_cards/baseball_cards_oneset.php?s='
checklist_end = 'top01'
#there is no page for 1973 so work around below
# and if extending to 1980 the file is top02

player_list = []
with open('data\ebay\player_list.txt','r') as reader:
    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        player_line = line.split(',')
        player_line1 = player_line[1].split('\n')
        player_line[1] = player_line1[0]
        player_list.append([player_line[0],player_line[1]])
        line = reader.readline()
#player_list = ['Aaron','Mantle','Morgan','Bench']
ebay_url = 'https://www.ebay.com/sch/i.html'
search_opts = '?_sacat=213' \
              '&_saslop=2&_dmd=1&_sasl=comc_consignment%2Cdeans_cards%2Cbbcexchange3%2C+starxcards%2Cgregmorriscards&_sop=10&_stpos=27587&LH_Time=1&_ftrt=903&_ftrv=48&LH_Auction=1'
base_text = '&_nkw=topps+'
base_excludes = '+-psa+-gai+-bgs+-gma+-sgc+-bvg+-bccg+-beckett+-fgs+-cga+-pro+-csa+-1982+-1996+-1997+-1998+-2001+-2003+-2020+-reprint+-lot+-gem+-game+-different+-cards'
grades = '+%284%2C5%2C6%2C7%2C8%2C9%29'

with open('data\ebay\search_list.txt','w') as writer:
    for year in range(start_year,end_year+1):
        if year == 1960:
            grades = '+%285%2C6%2C7%2C8%2C9%29'
        elif year == 1965:
            grades = '+%286%2C7%2C8%2C9%29'
        elif year == 1970:
            grades = '+%287%2C8%2C9%2C10%29'
        elif year == 1976:
            grades = '+%288%2C9%2C10%29'
        # there is no 1973 file so using 72 and adding schmidt (later)
        if year == 1973:
            url = checklist_url + '1972' + checklist_end
        else:
            url = checklist_url + str(year) + checklist_end
        r = requests.get(url)
        r_html = r.text
        soup = BeautifulSoup(r_html, 'lxml')
        for player in player_list:
            print_it = False
            for link in soup.find_all('a'):
                if player[0] in str(link.string):
                    print_it = True
                if ((player[0] == 'Schmidt' ) and (year == 1973)):
                    print_it = True
            if print_it:
                writer.write(player[0] + ": " + str(year) + '\n')
                writer.write(ebay_url + search_opts + base_text + player[0] + player[1] + grades + '+' + str(year) + base_excludes + '\n')

