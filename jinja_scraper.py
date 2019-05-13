import scraper_helper
from bs4 import BeautifulSoup


base_url = "https://shrine.mobi"
shrine_mobi_lists = [
    "https://shrine.mobi/area/hokkaido/hokkaido/",
    "https://shrine.mobi/area/tohoku/aomori/",
    "https://shrine.mobi/area/tohoku/akita/",
    "https://shrine.mobi/area/tohoku/yamagata/",
    "https://shrine.mobi/area/tohoku/iwate/",
    "https://shrine.mobi/area/tohoku/miyagi/",
    "https://shrine.mobi/area/tohoku/fukushima/",
    "https://shrine.mobi/area/kanto/tokyo/",
    "https://shrine.mobi/area/kanto/kanagawa/",
    "https://shrine.mobi/area/kanto/saitama/",
    "https://shrine.mobi/area/kanto/chiba/",
    "https://shrine.mobi/area/kanto/tochigi/",
    "https://shrine.mobi/area/kanto/ibaraki/",
    "https://shrine.mobi/area/kanto/gunma/",
    "https://shrine.mobi/area/koshinetsu/niigata/",
    "https://shrine.mobi/area/koshinetsu/yamanashi/",
    "https://shrine.mobi/area/koshinetsu/nagano/",
    "https://shrine.mobi/area/tokai/aichi/",
    "https://shrine.mobi/area/tokai/gifu/",
    "https://shrine.mobi/area/tokai/shizuoka/",
    "https://shrine.mobi/area/tokai/mie/",
    "https://shrine.mobi/area/hokuriku/ishikawa/",
    "https://shrine.mobi/area/hokuriku/toyama/",
    "https://shrine.mobi/area/hokuriku/fukui/",
    "https://shrine.mobi/area/kansai/osaka/",
    "https://shrine.mobi/area/kansai/hyogo/",
    "https://shrine.mobi/area/kansai/kyoto/",
    "https://shrine.mobi/area/kansai/shiga/",
    "https://shrine.mobi/area/kansai/nara/",
    "https://shrine.mobi/area/kansai/wakayama/",
    "https://shrine.mobi/area/chugoku/okayama/",
    "https://shrine.mobi/area/chugoku/hiroshima/",
    "https://shrine.mobi/area/chugoku/tottori/",
    "https://shrine.mobi/area/chugoku/shimane/",
    "https://shrine.mobi/area/chugoku/yamaguchi/",
    "https://shrine.mobi/area/shikoku/kagawa/",
    "https://shrine.mobi/area/shikoku/tokushima/",
    "https://shrine.mobi/area/shikoku/ehime/",
    "https://shrine.mobi/area/shikoku/kochi/",
    "https://shrine.mobi/area/kyushu/fukuoka/",
    "https://shrine.mobi/area/kyushu/saga/",
    "https://shrine.mobi/area/kyushu/nagasaki/",
    "https://shrine.mobi/area/kyushu/kumamoto/",
    "https://shrine.mobi/area/kyushu/oita/",
    "https://shrine.mobi/area/kyushu/miyazaki/",
    "https://shrine.mobi/area/kyushu/kagoshima/",
    "https://shrine.mobi/area/kyushu/okinawa/"
]


def process_one_prefecture(url):
    raw_html = scraper_helper.simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    linklist = html.find('ul', class_="linklist")
    num_pages = len(linklist.contents[1].contents)
    for i in range(num_pages):
        if i == 0:
            process_one_list(html.find('ul', class_="list_main"))
        else:
            raw_new_page = scraper_helper.simple_get(url + str(i + 1))
            new_page = BeautifulSoup(raw_new_page, 'html.parser')
            process_one_list(new_page.find('ul', class_="list_main"))


def process_one_list(jinja_list):
    for jinja in jinja_list:
        if jinja == '\n':
            continue

        jinja_url = jinja.contents[1].get('href')
        jinja_raw_html = scraper_helper.simple_get(base_url + jinja_url)
        if jinja_raw_html is not None:
            jinja_html = BeautifulSoup(jinja_raw_html, 'html.parser')
            jinja_name = jinja_html.find('span', itemprop="name")
            jinja_address_div = jinja_html.find('div', typeof="v:Address")
            with open('jinja.txt', 'a', encoding='utf-8') as file:
                file.write(jinja_name.string + ',' + jinja_address_div.contents[0].string + jinja_address_div.contents[1] + '\n')


for prefecture in shrine_mobi_lists:
    process_one_prefecture(prefecture)
