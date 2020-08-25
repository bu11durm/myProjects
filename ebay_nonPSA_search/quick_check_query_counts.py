import requests
from bs4 import BeautifulSoup

cards_per_row = 5

with open('data\search_hits.html','w') as hits_writer:
    hits_writer.write('<html><header><title>Search Hits</title></header>')
    hits_writer.write('<body><h1>Search Hits</h1><table><tr>')
    cards_in_row = 0
    with open('data\search_counts.html','w') as counts_writer:
        counts_writer.write('<html><header><title>Query Counts</title></header>')
        counts_writer.write('<body><h1>Query Counts</h1>')
        with open('data\search_list.txt','r') as reader:
            line = reader.readline()
            while line != '':  # The EOF char is an empty string
                line2 = reader.readline()
                print(line)
                r = requests.get(line2)
                r_html = r.text
                soup = BeautifulSoup(r_html, 'lxml')
                results = soup.body.find('div', attrs={'class': 'srp-controls__control srp-controls__count'})
                try:
                    span = results.h1.find_next('span')
                    span_found = True
                    counts_writer.write('<p>' + span.string + " hits for <a href=" + line2 + '>' + line + '</a>')
                except:
                    print('query error on ' + line)
                    span_found = False
                if ((span_found == True) & (int(span.string) > 0)):
                    list_items = soup.body.find_all('li', attrs={'class': 's-item',
                                                                 'data-view': lambda L: L and L.startswith('mi')})
                    for item in list_items:
                        if cards_in_row == 5:
                            hits_writer.write('</tr><tr>')
                            cards_in_row = 0
                        cards_in_row += 1
                        hits_writer.write('<td>')
                        item2 = item.div
                        next_divs = item2.find_all('div')
                        detail_div = next_divs[0].find_next_sibling('div')
                        image_div = next_divs[1]
                        thumbnail = image_div.find_next('img')
                        link = detail_div.find_next('a')
                        hits_writer.write('<a href=' + link['href'] + '><img height = 60% src =' + thumbnail['src'] + '><br>')
                        # hits_writer.write('<img height=60% src=' + thumbnail['src'] + '><br>')
                        hits_writer.write('<a href=' + link['href'] + '>' + line + '</a><br>')
                        hits_writer.write(detail_div.find_next('span', attrs={'s-item__bids s-item__bidCount'}).string + " ")
                        hits_writer.write(detail_div.find_next('span', attrs={'s-item__price'}).string)
                        # try:
                        #    hits_writer.write(detail_div.find_next('span', attrs={'s-item__bids s-item__bidCount'}).string)
                        # except:
                        #    print('no bidcount found')
                        hits_writer.write('</td>')
                line = reader.readline()
        counts_writer.write('</body></html>')
    hits_writer.write('</tr></table></body></html>')