from bs4 import BeautifulSoup
import requests


def smulweb_ingredients(url, tag):
    res = requests.get(url)
    page = BeautifulSoup(res.text, 'html.parser')
    select_tag = page.select(tag)
    select = select_tag[0]
    contents = select.contents
    everything = ""
    for content in contents:
        everything += content.__str__()
    replace = BeautifulSoup(everything, 'html.parser')
    p_tag = replace.p
    for a_tag in p_tag.select("a"):
        p_tag.a.unwrap()
    return replace.__str__()


def smulweb_instructions(url, tag):
    res = requests.get(url)
    page = BeautifulSoup(res.text, 'html.parser')
    select_tag = page.select(tag)
    select = select_tag[0]
    contents = select.contents
    everything = ""
    for content in contents:
        everything += content.__str__()
    new_page = BeautifulSoup(everything, 'html.parser')
    contents = new_page.contents

    h3 = new_page.select("div.h3")
    for div in h3:
        new_h3 = new_page.new_tag("h3")
        new_h3.string = div.string
        div.replace_with(new_h3)
    everything = ""
    for content in contents:
        everything += content.__str__()
    noscript = BeautifulSoup(everything, "html.parser")
    for script in noscript.select("script"):
        noscript.script.decompose()
    for no_a in noscript.select("a"):
        noscript.a.unwrap()
    return noscript.__str__()


def title(url):
    res = requests.get(url)
    page = BeautifulSoup(res.text, 'html.parser')
    return page.h1.contents[0]


