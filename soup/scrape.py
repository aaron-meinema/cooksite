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

    def _a_unwrap(self, select_tag):
        for non_tag in select_tag.select("a"):
            select_tag.a.unwrap()

    def _script_decompose(self, select_tag):
        for non_tag in select_tag.select("script"):
            select_tag.script.decompose()

    def _h3_decompose(self, select_tag):
        for non_tag in select_tag.select("h3"):
            select_tag.h3.decompose()


class SmulWeb(_Scrape):

    def __init__(self, url):
        super().__init__(url)

    def smulweb_ingredients(self):
        contents = self._select("div.ingredienten")
        everything = ""
        for content in contents:
            everything += str(content)
        replace = BeautifulSoup(everything, 'html.parser')
        self._a_unwrap(replace)
        return str(replace)


# def smulweb_instructions(url, tag):
#     select_tag = page.select(tag)
#     select = select_tag[0]
#     contents = select.contents
#     everything = ""
#     for content in contents:
#         everything += content.__str__()
#     new_page = BeautifulSoup(everything, 'html.parser')
#     contents = new_page.contents
#
#     h3 = new_page.select("div.h3")
#     for div in h3:
#         new_h3 = new_page.new_tag("h3")
#         new_h3.string = div.string
#         div.replace_with(new_h3)
#     everything = ""
#     for content in contents:
#         everything += content.__str__()
#     noscript = BeautifulSoup(everything, "html.parser")
#     for script in noscript.select("script"):
#         noscript.script.decompose()
#     for no_a in noscript.select("a"):
#         noscript.a.unwrap()
#     return noscript.__str__()

#def smulweb_ingredients(url, tag):
#    select_tag = page.select(tag)
#    select = select_tag[0]
#    contents = select.contents
#    everything = ""
#    for content in contents:
#        everything += content.__str__()
#    replace = BeautifulSoup(everything, 'html.parser')
#    p_tag = replace.p
#    for a_tag in p_tag.select("a"):
#        p_tag.a.unwrap()
#    return replace.__str__()

