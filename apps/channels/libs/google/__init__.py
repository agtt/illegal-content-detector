from googlesearch import search


class Google:
    def __init__(self):
        self.url_list = []
        self.report_list = []

    def getList(self,page=1):
        for url in search('hercai 12. bolum izle', stop=page * 10):
            self.url_list.append(url)
            print(url)
        return self.url_list

    def getSource(self):
        pass


g = Google()
g.getList()