<<<<<<< HEAD
import json
import os
import re
import time

import telebot
import emoji
from bs4 import BeautifulSoup

import config
import requests
from lxml import etree
import tt_USA
import tt_China

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36'}
movieurl = "https://ent.sina.com.cn/movie/top10bang/"

res = requests.get(url=movieurl, headers=headers).content
selector = etree.HTML(res)

chat_id = config.CHAT_ID
TOKEN = os.environ.get('TOKEN') or config.TGBOT_TOKEN
bot = telebot.TeleBot(TOKEN)
logger = config.setup_log()

photo_china = open("Mainland.PNG", "rb")
photo_usa = open("NorthAmerica.PNG", "rb")
photo_rg = open("rg.png", "rb")

baomihua = emoji.emojize(':popcorn:')
one = "1️⃣"
two = '2️⃣'
thr = '3️⃣'
four = '4️⃣'
five = '5️⃣'
six = '6️⃣'
seven = '7️⃣'
eight = '8️⃣'
nine = '9️⃣'
ten = '🔟'
up = '📈 '
movie1 = '🎬 '
movie2 = '📺'


@bot.message_handler(commands=['list_China'])
def send_photo1(message):
    film_list_China = tt_China.get_file_top_ten()

    date_China = selector.xpath('//*[@id="__liveLayoutContainer"]/div/div/div/div/div[2]/div/div[1]/div[2]/span/text()')
    date_China = date_China[0]
    date_China1 = date_China[-5:-3]
    date_China2 = date_China[-2:]

    name_China = []
    wk_money_China = []
    all_money_China = []
    for film in film_list_China:
        name_China.append(film.name)
        wk_money_China.append(film.wk_money)
        all_money_China.append(film.all_money)

    name_China_url = []
    name_China_url1 = []
    name_China_value = []
    name_China_value1 = []
    for name in name_China:
        url = "https://search.keepfrds.workers.dev/?search=" + name
        response = requests.get(url)
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        for mk in dict_json["payload"]["items"]:
            try:
                name_China_value1.append(str(mk["rating"]["value"]))
                name_China_url1.append(mk["url"])
            except KeyError:
                pass
        try:
            if name_China_value1[0] == "0":
                name_China_value.append("N/A")
            else:
                name_China_value.append(name_China_value1[0])
            name_China_url.append(name_China_url1[0])
        except:
            name_China_value.append("N/A")
            name_China_url.append("")
        name_China_value1 = []
        name_China_url1 = []
        time.sleep(20)

    for index in range(len(name_China)):
        name_China[index] = " " + name_China[index]

    msg = bot.send_photo(chat_id=chat_id, photo=photo_china, parse_mode='MARKDOWN',
                         caption=["#TopBoxOffice #Mainland #票房\n"
                                  "\n"
                                  + baomihua + " *内地票房周榜*（" + date_China1 + '月' + date_China2 + "日 | 人民币)\n"
                                                                                                "\n"
                                  + one + "[" + name_China[0] + "](" + name_China_url[0] + ")" + " (" +
                                  name_China_value[0] + ")\n"
                                                        "       " +
                                  wk_money_China[0] + "万 / " + all_money_China[
                                      0] + "万\n "
                                           "\n"
                                  + two + "[" + name_China[1] + "](" + name_China_url[1] + ")" + " (" +
                                  name_China_value[1] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      1] + "万 / " + all_money_China[1] + "万\n "
                                                                         "\n"
                                  + thr + "[" + name_China[2] + "](" + name_China_url[2] + ")" + " (" +
                                  name_China_value[2] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      2] + "万 / " + all_money_China[2] + "万\n "
                                                                         "\n"
                                  + four + "[" + name_China[3] + "](" + name_China_url[3] + ")" + " (" +
                                  name_China_value[3] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      3] + "万 / " + all_money_China[3] + "万\n "
                                                                         "\n"
                                  + five + "[" + name_China[4] + "](" + name_China_url[4] + ")" + " (" +
                                  name_China_value[4] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      4] + "万 / " + all_money_China[4] + "万\n "
                                                                         "\n"
                                  + six + "[" + name_China[5] + "](" + name_China_url[5] + ")" + " (" +
                                  name_China_value[5] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      5] + "万 / " + all_money_China[5] + "万\n "
                                                                         "\n"
                                  + seven + "[" + name_China[6] + "](" + name_China_url[6] + ")" + " (" +
                                  name_China_value[6] + ")\n"
                                                        "       " +
                                  wk_money_China[6] + "万 / " + all_money_China[
                                      6] + "万\n "
                                           "\n"
                                  + eight + "[" + name_China[7] + "](" + name_China_url[7] + ")" + " (" +
                                  name_China_value[7] + ")\n"
                                                        "       " +
                                  wk_money_China[7] + "万 / " + all_money_China[
                                      7] + "万\n "
                                           "\n"
                                  + nine + "[" + name_China[8] + "](" + name_China_url[8] + ")" + " (" +
                                  name_China_value[8] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      8] + "万 / " + all_money_China[8] + "万\n "
                                                                         "\n"
                                  + ten + "[" + name_China[9] + "](" + name_China_url[9] + ")" + " (" +
                                  name_China_value[9] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      9] + "万 / " + all_money_China[9] + "万\n "
                                                                         "\n"
                                                                         "*Channel:* [@Odyssey+](https://t.me/odysseyplus)"])
    bot.send_message(message.chat.id, "中国电影票房榜单已推送到Odyssey频道")
    bot.delete_message(chat_id, msg.message_id + 1)


@bot.message_handler(commands=['list_USA'])
def send_photo1(message):
    film_list = tt_USA.get_file_top_ten()
    date_USA = selector.xpath('//*[@id="__liveLayoutContainer"]/div/div/div/div/div[1]/div/div[1]/div[2]/span/text()')
    date_USA = date_USA[0]
    date_USA1 = date_USA[-5:-3]
    date_USA2 = date_USA[-2:]

    name_USA = []
    wk_money_USA = []
    all_money_USA = []
    for film in film_list:
        name_USA.append(film.name)
        wk_money_USA.append(film.wk_money)
        all_money_USA.append(film.all_money)

    wk_money_USA1 = []
    all_money_USA1 = []
    for i in wk_money_USA:
        i = i[:-4]
        wk_money_USA1.append(i)

    for i in all_money_USA:
        i = i[:-4]
        all_money_USA1.append(i)

    name_USA_url = []
    name_USA_url1 = []
    name_USA_value = []
    name_USA_value1 = []

    for name in name_USA:
        url = "https://search.keepfrds.workers.dev/?search=" + name
        response = requests.get(url)
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        for mk in dict_json["payload"]["items"]:
            try:
                name_USA_value1.append(str(mk["rating"]["value"]))
                name_USA_url1.append(mk["url"])
            except KeyError:
                pass
        try:
            if name_USA_value1[0] == "0":
                name_USA_value.append("N/A")
            else:
                name_USA_value.append(name_USA_value1[0])
            name_USA_url.append(name_USA_url1[0])
        except:
            name_USA_value.append("N/A")
            name_USA_url.append("")
        name_USA_value1 = []
        name_USA_url1 = []
        time.sleep(20)

    for index in range(len(name_USA)):
        name_USA[index] = " " + name_USA[index]

    msg = bot.send_photo(chat_id=chat_id, photo=photo_usa, parse_mode='MARKDOWN',
                         caption=["#TopBoxOffice #NorthAmerica #票房\n"
                                  "\n"
                                  + baomihua + " *北美票房周榜*（" + date_USA1 + "月" + date_USA2 + "日 | 美元)\n"
                                                                                            "\n"
                                  + one + "[" + name_USA[0] + "](" + name_USA_url[0] + ")" + " (" + name_USA_value[
                                      0] + ")\n"
                                           "       " + wk_money_USA1[
                                      0] + "万 / " + all_money_USA1[0] + "万\n "
                                                                        "\n"
                                  + two + "[" + name_USA[1] + "](" + name_USA_url[1] + ")" + " (" + name_USA_value[
                                      1] + ")\n"
                                           "       " + wk_money_USA1[
                                      1] + "万 / " + all_money_USA1[1] + "万\n "
                                                                        "\n"
                                  + thr + "[" + name_USA[2] + "](" + name_USA_url[2] + ")" + " (" + name_USA_value[
                                      2] + ")\n"
                                           "       " + wk_money_USA1[
                                      2] + "万 / " + all_money_USA1[2] + "万\n "
                                                                        "\n"
                                  + four + "[" + name_USA[3] + "](" + name_USA_url[3] + ")" + " (" + name_USA_value[
                                      3] + ")\n"
                                           "       " + wk_money_USA1[
                                      3] + "万 / " + all_money_USA1[3] + "万\n "
                                                                        "\n"
                                  + five + "[" + name_USA[4] + "](" + name_USA_url[4] + ")" + " (" + name_USA_value[
                                      4] + ")\n"
                                           "       " + wk_money_USA1[
                                      4] + "万 / " + all_money_USA1[4] + "万\n "
                                                                        "\n"
                                  + six + "[" + name_USA[5] + "](" + name_USA_url[5] + ")" + " (" + name_USA_value[
                                      5] + ")\n"
                                           "       " + wk_money_USA1[
                                      5] + "万 / " + all_money_USA1[5] + "万\n "
                                                                        "\n"
                                  + seven + "[" + name_USA[6] + "](" + name_USA_url[6] + ")" + " (" + name_USA_value[
                                      6] + ")\n"
                                           "       " +
                                  wk_money_USA1[6] + "万 / " + all_money_USA1[
                                      6] + "万\n "
                                           "\n"
                                  + eight + "[" + name_USA[7] + "](" + name_USA_url[7] + ")" + " (" + name_USA_value[
                                      7] + ")\n"
                                           "       " +
                                  wk_money_USA1[7] + "万 / " + all_money_USA1[
                                      7] + "万\n "
                                           "\n"
                                  + nine + "[" + name_USA[8] + "](" + name_USA_url[8] + ")" + " (" + name_USA_value[
                                      8] + ")\n"
                                           "       " + wk_money_USA1[
                                      8] + "万 / " + all_money_USA1[8] + "万\n "
                                                                        "\n"
                                  + ten + "[" + name_USA[9] + "](" + name_USA_url[9] + ")" + " (" + name_USA_value[
                                      9] + ")\n"
                                           "       " + wk_money_USA1[
                                      9] + "万 / " + all_money_USA1[9] + "万\n "
                                                                        "\n"
                                                                        "*Channel:* [@Odyssey+](https://t.me/odysseyplus)"])
    bot.send_message(message.chat.id, "美国电影票房榜单已推送到Odyssey频道")
    bot.delete_message(chat_id, msg.message_id + 1)


@bot.message_handler(commands=['list_Streaming'])
def send_rglist(message):
    listurl1 = "https://reelgood.com/movies/browse/popular-movies"
    page = requests.get(listurl1)
    soup = BeautifulSoup(page.content, "html.parser")
    list1 = soup.find_all("a", href=re.compile(r'/movie/'))
    movie_list_en = []
    for link in list1:
        movie_list_en.append(link.text)
    movie_list_en = [i for i in movie_list_en if i != '']

    movie_list_en1 = []
    for movie in movie_list_en:
        x = movie.split("SeeSeen It")
        movie_list_en1.append(x[-1])
    movie_list_en = movie_list_en1
    print(movie_list_en)

    movie_list_en1 = []
    for i in movie_list_en:
        movie_list_en1.append(i.replace(' ', ''))

    movie_list_zh = []
    movie_list_zh1 = []
    movie_list_value = []
    movie_list_value1 = []
    movie_list_url = []
    movie_list_url1 = []

    movie_list_en1 = movie_list_en1[:6]

    movie_list_en2 = []

    for movie in movie_list_en1:
        movie = movie.replace('(', '%20')
        movie = movie.replace(')', '')
        movie_list_en2.append(movie)
    movie_list_en1 = movie_list_en2
    print(movie_list_en1)

    for movie in movie_list_en1:
        url = "https://search.keepfrds.workers.dev/?search=" + movie
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36",
        }
        response = requests.get(url)
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        print(type(dict_json))

        try:
            for mk in dict_json["payload"]["items"]:
                try:
                    list = mk["title"].split(' ', 1)
                    if u'\u4e00' <= list[0] <= u'\u9fa5':
                        movie_list_zh1.append(list[0])
                        movie_list_value1.append(str(mk["rating"]["value"]))
                        movie_list_url1.append(mk["url"])
                except KeyError:
                    pass
            try:
                movie_list_zh.append(movie_list_zh1[0])
                if movie_list_value1[0] == "0":
                    movie_list_value.append("N/A")
                else:
                    movie_list_value.append(movie_list_value1[0])
                movie_list_url.append(movie_list_url1[0])
            except:
                movie_list_zh.append(movie)
                movie_list_value.append("N/A")
                movie_list_url.append("")
        except:
            movie_list_zh.append(movie)
            movie_list_value.append("N/A")
            movie_list_url.append("")
        movie_list_zh1 = []
        movie_list_value1 = []
        movie_list_url1 = []
        time.sleep(20)
    print(movie_list_zh)
    print(movie_list_value)
    print(movie_list_url)

    listurl2 = "https://reelgood.com/tv/curated/trending-picks"
    page = requests.get(listurl2)
    soup = BeautifulSoup(page.content, "html.parser")
    list2 = soup.find_all("a", href=re.compile(r'/show/'))
    show_list_en = []
    for link in list2:
        show_list_en.append(link.text)
    show_list_en = [i for i in show_list_en if i != '']

    show_list_en1 = []
    for show in show_list_en:
        x = show.split("TVTrack Series")
        show_list_en1.append(x[-1])
    show_list_en = show_list_en1
    print(show_list_en)

    show_list_en1 = []
    for i in show_list_en:
        show_list_en1.append(i.replace(' ', ''))

    show_list_zh = []
    show_list_zh1 = []
    show_list_value = []
    show_list_value1 = []
    show_list_url = []
    show_list_url1 = []

    show_list_en1 = show_list_en1[:6]

    show_list_en2 = []
    for show in show_list_en1:
        show = show.replace('(', '%20')
        show = show.replace(')', '')
        show_list_en2.append(show)
    show_list_en1 = show_list_en2
    print(show_list_en1)

    for show in show_list_en1:
        url = "https://search.keepfrds.workers.dev/?search=" + show
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36",
        }
        response = requests.get(url)
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        print(type(dict_json))

        try:
            for mk in dict_json["payload"]["items"]:
                try:
                    list = mk["title"].split(' ', 1)
                    if u'\u4e00' <= list[0] <= u'\u9fa5':
                        show_list_zh1.append(list[0])
                        show_list_value1.append(str(mk["rating"]["value"]))
                        show_list_url1.append(mk["url"])
                except KeyError:
                    pass
            try:
                show_list_zh.append(show_list_zh1[0])
                if show_list_value1[0] == "0":
                    show_list_value.append("N/A")
                else:
                    show_list_value.append(show_list_value1[0])
                show_list_url.append(show_list_url1[0])
            except:
                show_list_zh.append(show)
                show_list_value.append("N/A")
                show_list_url.append("")
        except:
            show_list_zh.append(show)
            show_list_value.append("N/A")
            show_list_url.append("")
        show_list_zh1 = []
        show_list_value1 = []
        show_list_url1 = []
        time.sleep(20)

    print(show_list_zh)
    print(show_list_value)
    print(show_list_url)

    msg = bot.send_photo(chat_id=chat_id, photo=photo_rg, parse_mode='MARKDOWN',
                         caption=["#TrendingNow #Streaming\n" + "\n" +
                                  up + "*流媒体热度排行*（" + time.strftime("%m", time.localtime()) + "月" + time.strftime(
                             "%d", time.localtime()) + "日)" + "\n" + "\n" +
                                  movie1 + "*电影 Movies*\n" + "\n" +
                                  one + " [" + movie_list_zh[0] + "](" + movie_list_url[
                                      0] + ")" + " (" + movie_list_value[0] + ")\n" + "\n" +
                                  two + " [" + movie_list_zh[1] + "](" + movie_list_url[
                                      1] + ")" + " (" + movie_list_value[1] + ")\n" + "\n" +
                                  thr + " [" + movie_list_zh[2] + "](" + movie_list_url[
                                      2] + ")" + " (" + movie_list_value[2] + ")\n" + "\n" +
                                  four + " [" + movie_list_zh[3] + "](" + movie_list_url[
                                      3] + ")" + " (" + movie_list_value[3] + ")\n" + "\n" +
                                  five + " [" + movie_list_zh[4] + "](" + movie_list_url[
                                      4] + ")" + " (" + movie_list_value[4] + ")\n" + "\n" +
                                  six + " [" + movie_list_zh[5] + "](" + movie_list_url[
                                      5] + ")" + " (" + movie_list_value[5] + ")\n" + "\n" +
                                  movie2 + " *剧集 TV Shows*\n" + "\n" +
                                  one + " [" + show_list_zh[0] + "](" + show_list_url[
                                      0] + ")" + " (" + show_list_value[0] + ")\n" + "\n" +
                                  two + " [" + show_list_zh[1] + "](" + show_list_url[
                                      1] + ")" + " (" + show_list_value[1] + ")\n" + "\n" +
                                  thr + " [" + show_list_zh[2] + "](" + show_list_url[
                                      2] + ")" + " (" + show_list_value[2] + ")\n" + "\n" +
                                  four + " [" + show_list_zh[3] + "](" + show_list_url[
                                      3] + ")" + " (" + show_list_value[3] + ")\n" + "\n" +
                                  five + " [" + show_list_zh[4] + "](" + show_list_url[
                                      4] + ")" + " (" + show_list_value[4] + ")\n" + "\n" +
                                  six + " [" + show_list_zh[5] + "](" + show_list_url[
                                      5] + ")" + " (" + show_list_value[5] + ")\n" + "\n" +
                                  "*Channel:* [@Odyssey+](https://t.me/odysseyplus)"])
    bot.send_message(message.chat.id, "流媒体热度排行已推送到Odyssey频道")
    bot.delete_message(chat_id, msg.message_id + 1)


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, timeout=600)
    except Exception as e:
        logger.exception("__main__ Telegram Bot运行异常，抛出信息:{}".format(e))
=======
import json
import os
import re
import time

import telebot
import emoji
from bs4 import BeautifulSoup

import config
import requests
from lxml import etree
import tt_USA
import tt_China

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.88 Safari/537.36'}
movieurl = "https://ent.sina.com.cn/movie/top10bang/"

res = requests.get(url=movieurl, headers=headers).content
selector = etree.HTML(res)

chat_id = config.CHAT_ID
TOKEN = os.environ.get('TOKEN') or config.TGBOT_TOKEN
bot = telebot.TeleBot(TOKEN)
logger = config.setup_log()

photo_china = open("Mainland.PNG", "rb")
photo_usa = open("NorthAmerica.PNG", "rb")
photo_rg = open("rg.png", "rb")

baomihua = emoji.emojize(':popcorn:')
one = "1️⃣"
two = '2️⃣'
thr = '3️⃣'
four = '4️⃣'
five = '5️⃣'
six = '6️⃣'
seven = '7️⃣'
eight = '8️⃣'
nine = '9️⃣'
ten = '🔟'
up = '📈 '
movie1 = '🎬 '
movie2 = '📺'


@bot.message_handler(commands=['list_China'])
def send_photo1(message):
    film_list_China = tt_China.get_file_top_ten()

    date_China = selector.xpath('//*[@id="__liveLayoutContainer"]/div/div/div/div/div[2]/div/div[1]/div[2]/span/text()')
    date_China = date_China[0]
    date_China1 = date_China[-5:-3]
    date_China2 = date_China[-2:]

    name_China = []
    wk_money_China = []
    all_money_China = []
    for film in film_list_China:
        name_China.append(film.name)
        wk_money_China.append(film.wk_money)
        all_money_China.append(film.all_money)

    name_China_url = []
    name_China_url1 = []
    name_China_value = []
    name_China_value1 = []
    for name in name_China:
        url = "https://search.keepfrds.workers.dev/?search=" + name
        response = requests.get(url)
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        for mk in dict_json["payload"]["items"]:
            try:
                name_China_value1.append(str(mk["rating"]["value"]))
                name_China_url1.append(mk["url"])
            except KeyError:
                pass
        try:
            if name_China_value1[0] == "0":
                name_China_value.append("N/A")
            else:
                name_China_value.append(name_China_value1[0])
            name_China_url.append(name_China_url1[0])
        except:
            name_China_value.append("N/A")
            name_China_url.append("")
        name_China_value1 = []
        name_China_url1 = []
        time.sleep(20)

    for index in range(len(name_China)):
        name_China[index] = " " + name_China[index]

    msg = bot.send_photo(chat_id=chat_id, photo=photo_china, parse_mode='MARKDOWN',
                         caption=["#TopBoxOffice #Mainland #票房\n"
                                  "\n"
                                  + baomihua + " *内地票房周榜*（" + date_China1 + '月' + date_China2 + "日 | 人民币)\n"
                                                                                                "\n"
                                  + one + "[" + name_China[0] + "](" + name_China_url[0] + ")" + " (" +
                                  name_China_value[0] + ")\n"
                                                        "       " +
                                  wk_money_China[0] + "万 / " + all_money_China[
                                      0] + "万\n "
                                           "\n"
                                  + two + "[" + name_China[1] + "](" + name_China_url[1] + ")" + " (" +
                                  name_China_value[1] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      1] + "万 / " + all_money_China[1] + "万\n "
                                                                         "\n"
                                  + thr + "[" + name_China[2] + "](" + name_China_url[2] + ")" + " (" +
                                  name_China_value[2] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      2] + "万 / " + all_money_China[2] + "万\n "
                                                                         "\n"
                                  + four + "[" + name_China[3] + "](" + name_China_url[3] + ")" + " (" +
                                  name_China_value[3] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      3] + "万 / " + all_money_China[3] + "万\n "
                                                                         "\n"
                                  + five + "[" + name_China[4] + "](" + name_China_url[4] + ")" + " (" +
                                  name_China_value[4] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      4] + "万 / " + all_money_China[4] + "万\n "
                                                                         "\n"
                                  + six + "[" + name_China[5] + "](" + name_China_url[5] + ")" + " (" +
                                  name_China_value[5] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      5] + "万 / " + all_money_China[5] + "万\n "
                                                                         "\n"
                                  + seven + "[" + name_China[6] + "](" + name_China_url[6] + ")" + " (" +
                                  name_China_value[6] + ")\n"
                                                        "       " +
                                  wk_money_China[6] + "万 / " + all_money_China[
                                      6] + "万\n "
                                           "\n"
                                  + eight + "[" + name_China[7] + "](" + name_China_url[7] + ")" + " (" +
                                  name_China_value[7] + ")\n"
                                                        "       " +
                                  wk_money_China[7] + "万 / " + all_money_China[
                                      7] + "万\n "
                                           "\n"
                                  + nine + "[" + name_China[8] + "](" + name_China_url[8] + ")" + " (" +
                                  name_China_value[8] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      8] + "万 / " + all_money_China[8] + "万\n "
                                                                         "\n"
                                  + ten + "[" + name_China[9] + "](" + name_China_url[9] + ")" + " (" +
                                  name_China_value[9] + ")\n"
                                                        "       " +
                                  wk_money_China[
                                      9] + "万 / " + all_money_China[9] + "万\n "
                                                                         "\n"
                                                                         "*Channel:* [@Odyssey+](https://t.me/odysseyplus)"])
    bot.send_message(message.chat.id, "中国电影票房榜单已推送到Odyssey频道")
    bot.delete_message(chat_id, msg.message_id + 1)


@bot.message_handler(commands=['list_USA'])
def send_photo1(message):
    film_list = tt_USA.get_file_top_ten()
    date_USA = selector.xpath('//*[@id="__liveLayoutContainer"]/div/div/div/div/div[1]/div/div[1]/div[2]/span/text()')
    date_USA = date_USA[0]
    date_USA1 = date_USA[-5:-3]
    date_USA2 = date_USA[-2:]

    name_USA = []
    wk_money_USA = []
    all_money_USA = []
    for film in film_list:
        name_USA.append(film.name)
        wk_money_USA.append(film.wk_money)
        all_money_USA.append(film.all_money)

    wk_money_USA1 = []
    all_money_USA1 = []
    for i in wk_money_USA:
        i = i[:-4]
        wk_money_USA1.append(i)

    for i in all_money_USA:
        i = i[:-4]
        all_money_USA1.append(i)

    name_USA_url = []
    name_USA_url1 = []
    name_USA_value = []
    name_USA_value1 = []

    for name in name_USA:
        url = "https://search.keepfrds.workers.dev/?search=" + name
        response = requests.get(url)
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        for mk in dict_json["payload"]["items"]:
            try:
                name_USA_value1.append(str(mk["rating"]["value"]))
                name_USA_url1.append(mk["url"])
            except KeyError:
                pass
        try:
            if name_USA_value1[0] == "0":
                name_USA_value.append("N/A")
            else:
                name_USA_value.append(name_USA_value1[0])
            name_USA_url.append(name_USA_url1[0])
        except:
            name_USA_value.append("N/A")
            name_USA_url.append("")
        name_USA_value1 = []
        name_USA_url1 = []
        time.sleep(20)

    for index in range(len(name_USA)):
        name_USA[index] = " " + name_USA[index]

    msg = bot.send_photo(chat_id=chat_id, photo=photo_usa, parse_mode='MARKDOWN',
                         caption=["#TopBoxOffice #NorthAmerica #票房\n"
                                  "\n"
                                  + baomihua + " *北美票房周榜*（" + date_USA1 + "月" + date_USA2 + "日 | 美元)\n"
                                                                                            "\n"
                                  + one + "[" + name_USA[0] + "](" + name_USA_url[0] + ")" + " (" + name_USA_value[
                                      0] + ")\n"
                                           "       " + wk_money_USA1[
                                      0] + "万 / " + all_money_USA1[0] + "万\n "
                                                                        "\n"
                                  + two + "[" + name_USA[1] + "](" + name_USA_url[1] + ")" + " (" + name_USA_value[
                                      1] + ")\n"
                                           "       " + wk_money_USA1[
                                      1] + "万 / " + all_money_USA1[1] + "万\n "
                                                                        "\n"
                                  + thr + "[" + name_USA[2] + "](" + name_USA_url[2] + ")" + " (" + name_USA_value[
                                      2] + ")\n"
                                           "       " + wk_money_USA1[
                                      2] + "万 / " + all_money_USA1[2] + "万\n "
                                                                        "\n"
                                  + four + "[" + name_USA[3] + "](" + name_USA_url[3] + ")" + " (" + name_USA_value[
                                      3] + ")\n"
                                           "       " + wk_money_USA1[
                                      3] + "万 / " + all_money_USA1[3] + "万\n "
                                                                        "\n"
                                  + five + "[" + name_USA[4] + "](" + name_USA_url[4] + ")" + " (" + name_USA_value[
                                      4] + ")\n"
                                           "       " + wk_money_USA1[
                                      4] + "万 / " + all_money_USA1[4] + "万\n "
                                                                        "\n"
                                  + six + "[" + name_USA[5] + "](" + name_USA_url[5] + ")" + " (" + name_USA_value[
                                      5] + ")\n"
                                           "       " + wk_money_USA1[
                                      5] + "万 / " + all_money_USA1[5] + "万\n "
                                                                        "\n"
                                  + seven + "[" + name_USA[6] + "](" + name_USA_url[6] + ")" + " (" + name_USA_value[
                                      6] + ")\n"
                                           "       " +
                                  wk_money_USA1[6] + "万 / " + all_money_USA1[
                                      6] + "万\n "
                                           "\n"
                                  + eight + "[" + name_USA[7] + "](" + name_USA_url[7] + ")" + " (" + name_USA_value[
                                      7] + ")\n"
                                           "       " +
                                  wk_money_USA1[7] + "万 / " + all_money_USA1[
                                      7] + "万\n "
                                           "\n"
                                  + nine + "[" + name_USA[8] + "](" + name_USA_url[8] + ")" + " (" + name_USA_value[
                                      8] + ")\n"
                                           "       " + wk_money_USA1[
                                      8] + "万 / " + all_money_USA1[8] + "万\n "
                                                                        "\n"
                                  + ten + "[" + name_USA[9] + "](" + name_USA_url[9] + ")" + " (" + name_USA_value[
                                      9] + ")\n"
                                           "       " + wk_money_USA1[
                                      9] + "万 / " + all_money_USA1[9] + "万\n "
                                                                        "\n"
                                                                        "*Channel:* [@Odyssey+](https://t.me/odysseyplus)"])
    bot.send_message(message.chat.id, "美国电影票房榜单已推送到Odyssey频道")
    bot.delete_message(chat_id, msg.message_id + 1)


@bot.message_handler(commands=['list_Streaming'])
def send_rglist(message):
    listurl1 = "https://reelgood.com/movies/browse/popular-movies"
    page = requests.get(listurl1)
    soup = BeautifulSoup(page.content, "html.parser")
    list1 = soup.find_all("a", href=re.compile(r'/movie/'))
    movie_list_en = []
    for link in list1:
        movie_list_en.append(link.text)
    movie_list_en = [i for i in movie_list_en if i != '']

    movie_list_en1 = []
    for movie in movie_list_en:
        x = movie.split("SeeSeen It")
        movie_list_en1.append(x[-1])
    movie_list_en = movie_list_en1
    print(movie_list_en)

    movie_list_en1 = []
    for i in movie_list_en:
        movie_list_en1.append(i.replace(' ', ''))
    print(movie_list_en1)

    movie_list_zh = []
    movie_list_zh1 = []
    movie_list_value = []
    movie_list_value1 = []
    movie_list_url = []
    movie_list_url1 = []

    movie_list_en1 = movie_list_en1[:6]

    for movie in movie_list_en1:
        url = "https://search.keepfrds.workers.dev/?search=" + movie
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36",
        }
        response = requests.get(url)
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        print(type(dict_json))

        for mk in dict_json["payload"]["items"]:
            try:
                list = mk["title"].split(' ', 1)
                if u'\u4e00' <= list[0] <= u'\u9fa5':
                    movie_list_zh1.append(list[0])
                    movie_list_value1.append(str(mk["rating"]["value"]))
                    movie_list_url1.append(mk["url"])
            except KeyError:
                pass
        try:
            movie_list_zh.append(movie_list_zh1[0])
            if movie_list_value1[0] == "0":
                movie_list_value.append("N/A")
            else:
                movie_list_value.append(movie_list_value1[0])
            movie_list_url.append(movie_list_url1[0])
        except:
            movie_list_zh.append(movie)
            movie_list_value.append("N/A")
            movie_list_url.append("")
        movie_list_zh1 = []
        movie_list_value1 = []
        movie_list_url1 = []
        time.sleep(20)
    print(movie_list_zh)
    print(movie_list_value)
    print(movie_list_url)

    listurl2 = "https://reelgood.com/tv/curated/trending-picks"
    page = requests.get(listurl2)
    soup = BeautifulSoup(page.content, "html.parser")
    list2 = soup.find_all("a", href=re.compile(r'/show/'))
    show_list_en = []
    for link in list2:
        show_list_en.append(link.text)
    show_list_en = [i for i in show_list_en if i != '']

    show_list_en1 = []
    for show in show_list_en:
        x = show.split("TVTrack Series")
        show_list_en1.append(x[-1])
    show_list_en = show_list_en1
    print(show_list_en)

    show_list_en1 = []
    for i in show_list_en:
        show_list_en1.append(i.replace(' ', ''))
    print(show_list_en1)

    show_list_zh = []
    show_list_zh1 = []
    show_list_value = []
    show_list_value1 = []
    show_list_url = []
    show_list_url1 = []

    show_list_en1 = show_list_en1[:6]

    for show in show_list_en1:
        url = "https://search.keepfrds.workers.dev/?search=" + show
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36",
        }
        response = requests.get(url)
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        print(type(dict_json))

        for mk in dict_json["payload"]["items"]:
            try:
                list = mk["title"].split(' ', 1)
                if u'\u4e00' <= list[0] <= u'\u9fa5':
                    show_list_zh1.append(list[0])
                    show_list_value1.append(str(mk["rating"]["value"]))
                    show_list_url1.append(mk["url"])
            except KeyError:
                pass
        try:
            show_list_zh.append(show_list_zh1[0])
            if show_list_value1[0] == "0":
                show_list_value.append("N/A")
            else:
                show_list_value.append(show_list_value1[0])
            show_list_url.append(show_list_url1[0])
        except:
            show_list_zh.append(show)
            show_list_value.append("N/A")
            show_list_url.append("")
        show_list_zh1 = []
        show_list_value1 = []
        show_list_url1 = []
        time.sleep(20)
    print(show_list_zh)
    print(show_list_value)
    print(show_list_url)

    msg = bot.send_photo(chat_id=chat_id, photo=photo_rg, parse_mode='MARKDOWN',
                         caption=["#TrendingNow #Streaming\n" + "\n" +
                                  up + "*流媒体热度排行*（" + time.strftime("%m", time.localtime()) + "月" + time.strftime(
                             "%d", time.localtime()) + "日)" + "\n" + "\n" +
                                  movie1 + "*电影 Movies*\n" + "\n" +
                                  one + " [" + movie_list_zh[0] + "](" + movie_list_url[
                                      0] + ")" + " (" + movie_list_value[0] + ")\n" + "\n" +
                                  two + " [" + movie_list_zh[1] + "](" + movie_list_url[
                                      1] + ")" + " (" + movie_list_value[1] + ")\n" + "\n" +
                                  thr + " [" + movie_list_zh[2] + "](" + movie_list_url[
                                      2] + ")" + " (" + movie_list_value[2] + ")\n" + "\n" +
                                  four + " [" + movie_list_zh[3] + "](" + movie_list_url[
                                      3] + ")" + " (" + movie_list_value[3] + ")\n" + "\n" +
                                  five + " [" + movie_list_zh[4] + "](" + movie_list_url[
                                      4] + ")" + " (" + movie_list_value[4] + ")\n" + "\n" +
                                  six + " [" + movie_list_zh[5] + "](" + movie_list_url[
                                      5] + ")" + " (" + movie_list_value[5] + ")\n" + "\n" +
                                  movie2 + " *剧集 TV Shows*\n" + "\n" +
                                  one + " [" + show_list_zh[0] + "](" + show_list_url[
                                      0] + ")" + " (" + show_list_value[0] + ")\n" + "\n" +
                                  two + " [" + show_list_zh[1] + "](" + show_list_url[
                                      1] + ")" + " (" + show_list_value[1] + ")\n" + "\n" +
                                  thr + " [" + show_list_zh[2] + "](" + show_list_url[
                                      2] + ")" + " (" + show_list_value[2] + ")\n" + "\n" +
                                  four + " [" + show_list_zh[3] + "](" + show_list_url[
                                      3] + ")" + " (" + show_list_value[3] + ")\n" + "\n" +
                                  five + " [" + show_list_zh[4] + "](" + show_list_url[
                                      4] + ")" + " (" + show_list_value[4] + ")\n" + "\n" +
                                  six + " [" + show_list_zh[5] + "](" + show_list_url[
                                      5] + ")" + " (" + show_list_value[5] + ")\n" + "\n" +
                                  "*Channel:* [@Odyssey+](https://t.me/odysseyplus)"])
    bot.send_message(message.chat.id, "流媒体热度排行已推送到Odyssey频道")
    bot.delete_message(chat_id, msg.message_id + 1)


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, timeout=600)
    except Exception as e:
        logger.exception("__main__ Telegram Bot运行异常，抛出信息:{}".format(e))
>>>>>>> b5263e1170dca3d06e9998dd687df4f84c0b6834
