

class Google:
    def __init__(self, keyword=None, page=1):
        self.keyword = keyword
        self.page = page
        self.url_list = []
        self.report_list = []

    def getlist(self):
        for url in search(self.keyword, stop=self.page * 10):
            self.url_list.append(url)
            print(url)
        return self.url_list
