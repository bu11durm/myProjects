
class Found_card:

    def __init__(self, headline, href, thumbnail, bidCount, price):
        self.headline = headline
        self.href = href
        self.thumbnail = thumbnail
        self.bidCount = bidCount
        self.price = price

    def print_card_cell(self,hits_writer):
        hits_writer.write('<td>')
        hits_writer.write('<a href=' + self.href + '><img height = 60% src =' + self.thumbnail + '><br>')
        hits_writer.write('<a href=' + self.href + '>' + self.headline + '</a><br>')
        hits_writer.write(self.bidCount + " " + self.price + "</td>")
        return