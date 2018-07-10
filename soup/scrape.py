from bs4 import BeautifulSoup
import requests


class _Scrape:

    def __init__(self, url):
        self.res = requests.get(url)
        self.page = BeautifulSoup(self.res.text, 'html.parser')
        self.url = url

    def __str__(self):
        return self.page.h1.contents[0]

    def _select(self, tag):
        select_tag = self.page.select(tag)
        select = select_tag[0]
        contents = select.contents
        return contents

    @staticmethod
    def _a_unwrap(select_tag):
        for _ in select_tag.select("a"):
            select_tag.a.unwrap()

    @staticmethod
    def _div_unwrap(select_tag):
        for _ in select_tag.select("div"):
            select_tag.div.unwrap()

    @staticmethod
    def _p_unwrap(select_tag):
        for _ in select_tag.select("p"):
            select_tag.p.unwrap()

    @staticmethod
    def _script_decompose(select_tag):
        for _ in select_tag.select("script"):
            select_tag.script.decompose()

    @staticmethod
    def _h3_decompose(select_tag):
        for _ in select_tag.select("h3"):
            select_tag.h3.decompose()

    @staticmethod
    def _br_extract(select_tag):
        for _ in select_tag.select("br"):
            select_tag.br.extract()

    @staticmethod
    def _everything(contents):
        everything = ""
        for content in contents:
            everything += str(content)
        return everything

    def split_lines(self, input):
        soup_list = input.splitlines()
        dictionary = dict()
        for item in soup_list:
            dictionary[str(item)] = "p"
        return dictionary


class SmulWeb(_Scrape):

    def __init__(self, url):
        super().__init__(url)

    def smulweb_ingredients(self):
        contents = self._select("div.ingredienten")
        everything = self._everything(contents)
        replace = BeautifulSoup(everything, 'html.parser')
        self._a_unwrap(replace)
        return str(replace)

    def smulweb_instructions(self):
        select_tag = self._select("div.itemprop_instructions")
        everything = self._everything(select_tag)
        new_page = BeautifulSoup(everything, 'html.parser')
        contents = new_page.contents
        self._everything(contents)
        stripped = BeautifulSoup(everything, "html.parser")
        self._script_decompose(stripped)
        self._a_unwrap(stripped)
        self._p_unwrap(stripped)
        self._br_extract(stripped)
        return str(stripped)

    def split_lines(self, input):
        soup_list = input.splitlines()
        dictionary = dict()
        for item in soup_list:
            soup = BeautifulSoup(item, "html.parser")
            if soup.find("div") is None:
                dictionary[str(item)] = "p"
            else:
                self._div_unwrap(soup)
                dictionary[str(soup)] = "h3"
        return dictionary

