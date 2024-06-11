import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = "https://www.ptt.cc/bbs/NBA/index.html"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("div", class_="r-ent")
data_list = []

for a in articles:
    data = {}
    title = a.find("div", class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "no title"
    data["標題"] = title

    popular = a.find("div", class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"
    data["人氣"] = popular

    date = a.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    data["日期"] = date
    data_list.append(data)

with open("ptt_nba_data.json", "w", encoding="utf-8") as file:
    json.dump(data_list, file, ensure_ascii = False, indent = 4)

#print(data_list)

    #print(f"標題:{title} 人氣:{popular} 日期:{date}")

#response = requests.get(url)
#print(response.text)
#if response.status_code == 200:
#    with open('output.html', 'w', encoding = 'utf-8') as f:
#        f.write(response.text)
#    print("寫入成功!")
#else:
#    print("沒有抓到網頁")





