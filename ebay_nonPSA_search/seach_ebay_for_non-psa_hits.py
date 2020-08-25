import requests
from bs4 import BeautifulSoup
import found_card
import datetime
from card_create import create_card

cards_per_row = 5
query_errors = 0
query_error_file = 'search_errors.txt'

# real list of queries
search_list = 'data\search_list.txt'
# test list of queries
# search_list = 'data\ebay\\test_search_list.txt'

with open('data\search_hits.html', 'w') as hits_writer:
    hits_writer.write('<html><header><title>Search Hits</title></header>')
    hits_writer.write('<body><h1>Search Hits</h1><table><tr>')
    cards_in_row = 0
    with open('data\search_counts.html', 'w') as counts_writer:
        counts_writer.write('<html><header><title>Query Counts</title></header>')
        counts_writer.write('<body><h1>Query Counts</h1>')
        with open(search_list, 'r') as reader:
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
#                    line_words = line.split(': ')
#                    driver.save_screenshot(
#                        'data/ebay/' + str(datetime.date.today()) + '_' + line_words[0] + '_' + line_words[1] + '.png')
                    query_errors += 1
                    with open('data\search_errors.txt', 'a') as error_writer:
                        error_writer.write('\n' + str(datetime.date.today()) + ' query error on: ' + line)
                    span_found = False
                if ((span_found == True) & (int(span.string) > 0)):
                    list_items = soup.body.find_all('li', attrs={'class': 's-item',
                                                                 'data-view': lambda L: L and L.startswith('mi')})
                    for item in list_items:
                        if cards_in_row == 5:
                            hits_writer.write('</tr><tr>')
                            cards_in_row = 0
                        cards_in_row += 1
                        item2 = item.div
                        found_card = create_card(line, item2)
                        found_card.print_card_cell(hits_writer)

                line = reader.readline()
        counts_writer.write('</body></html>')
    hits_writer.write('</tr></table>')
    hits_writer.write('<p>' + str(query_errors) + " <a href=" + query_error_file + '>query errors</a> for this run')
    hits_writer.write('</body></html>')
