import math
import re
import time
import requests
import json
from bs4 import BeautifulSoup

wk = str((math.trunc(time.localtime()[7] / 7 + 1)) - 1)
year = str(time.localtime()[0])

URL = "https://www.boxofficemojo.com/weekend/" + year + "W" + wk + "/?ref_=bo_hm_rw"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34",
}
page = requests.get(URL, headers=headers)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.content, "html.parser")
list1 = soup.find_all("a", href=re.compile(r'/release/'))
movie_name_list = []
for list2 in list1:
    movie_name_list.append(list2.text)
movie_boxsum_list = []
list3 = soup.find_all("td", attrs={"class": "a-text-right mojo-field-type-money mojo-estimatable"})
for list4 in list3:
    movie_boxsum_list.append(list4.text)
movie_boxsum_list1 = []
for s in movie_boxsum_list:
    s = s.replace('$', '')
    s = s.replace(',', '')
    movie_boxsum_list1.append(s)
movie_boxsum_list_gross = movie_boxsum_list1[::3]
movie_boxsum_list_total_gross = movie_boxsum_list1[2::3]
movie_boxsum_list_gross = movie_boxsum_list_gross[0:10:]
movie_boxsum_list_total_gross = movie_boxsum_list_total_gross[0:10]
movie_name_list = movie_name_list[0:10:]

wk_money_USA1 = []
all_money_USA1 = []
for i in movie_boxsum_list_gross:
    i = i[:-4]
    i = i + "万"
    wk_money_USA1.append(i)

for i in movie_boxsum_list_total_gross:
    i = i[:-4]
    i = i + "万"
    all_money_USA1.append(i)

movie_list_zh = []
movie_list_zh1 = []
movie_list_value = []
movie_list_value1 = []
movie_list_url = []
movie_list_url1 = []

for movie in movie_name_list:
    try:
        url = "https://search.keepfrds.workers.dev/?search=" + movie
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36",
        }
        response = requests.get(url)
        json_response = response.content.decode()
        dict_json = json.loads(json_response)
        print(type(dict_json))
    except:
        movie_list_zh.append(movie)
        movie_list_value.append("N/A")
        movie_list_url.append("")

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

for index in range(len(movie_name_list)):
    movie_name_list[index] = " " + movie_name_list[index]

print(movie_name_list)
print(wk_money_USA1)
print(all_money_USA1)
print(movie_list_zh)
print(movie_list_value)
print(movie_list_url)

# bom = bom.BoxOfficeMojo()
# print(bom.get_latest_weekend_stats())

# movie_name_cn = []
# movie_sum_num_cn = []
# movie_box_rate_cn = []
# movie_release_days_cn = []
# movie_box_desc_cn = []
#
# url = "https://piaofang.maoyan.com/getBoxList?date=1&isSplit=true"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34",
# }
# page = requests.get(url, headers=headers)
# page.encoding = 'utf-8'
# json_response = page.content.decode()
# print(json_response)
# dict_json = json.loads(json_response)
# for mk in dict_json["boxOffice"]["data"]["list"]:
#     movie_name_cn.append(mk["movieInfo"]["movieName"])
#     movie_box_rate_cn.append(mk["showCountRate"])
#     movie_sum_num_cn.append(mk["sumBoxDesc"])
#     movie_release_days_cn.append(mk["movieInfo"]["releaseInfo"])
#     movie_box_desc_cn.append(mk["boxDesc"])
# print(movie_name_cn)
# print(movie_release_days_cn)
# print(movie_box_rate_cn)
# print(movie_sum_num_cn)
# print(movie_box_desc_cn)
