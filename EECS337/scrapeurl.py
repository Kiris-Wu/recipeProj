import requests
from bs4 import BeautifulSoup as bs
import re
import random
def generalurl(topic,length):
    url = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    }

    for i in range(1, length):
        newurl = topic + str(i)
        cont = requests.get(newurl, timeout=150, headers=headers).content

        soup = bs(cont, "html.parser")

        resultlist = soup.find_all("a", href=True)

        if resultlist:
            for a in resultlist:

                result = re.search("(.*)/recipe/(\d+)/(.+)", a['href'])
                if (result):
                    thisurl = "https://www.allrecipes.com" + "/recipe/" + result.group(2) + "/" + result.group(3)
                    if (thisurl not in url):
                        url.append(thisurl)
                        print(thisurl)
    return url

def chineseurl():
    chineseUrl = "https://www.allrecipes.com/recipes/695/world-cuisine/asian/chinese/?page="
    url=generalurl(chineseUrl,10)
    return url

def japaneseurl():
    japaneseUrl = "https://www.allrecipes.com/recipes/699/world-cuisine/asian/japanese/?internalSource=hubcard&referringContentType=search%20results&clickId=cardslot%201&page="
    url=generalurl(japaneseUrl,10)
    return url

def veganurl():
    veganUrl = "https://www.allrecipes.com/recipes/1227/everyday-cooking/vegan/?internalSource=hubcard&referringContentType=search%20results&clickId=cardslot%201&page="
    url = generalurl(veganUrl,20)
    return url

def vegetarianurl():
    vegetarianUrl = "https://www.allrecipes.com/recipes/87/everyday-cooking/vegetarian/?internalSource=hubcard&referringContentType=search%20results&clickId=cardslot%201&page="
    url = generalurl(vegetarianUrl,20)
    return url

def mandpurl():
    mandpUrl = "https://www.allrecipes.com/search/results/?wt=meat&sort=re&page="
    url = generalurl(mandpUrl,20)
    return url

def seafoodurl():
    seafoodUrl="https://www.allrecipes.com/recipes/93/seafood/?internalSource=hubcard&referringContentType=search%20results&clickId=cardslot%201&page="
    url = generalurl(seafoodUrl, 20)
    return url

def fruitandvurl():
    fruitandvUrl = "https://www.allrecipes.com/recipes/1058/fruits-and-vegetables/fruits/?internalSource=hubcard&referringContentType=search%20results&clickId=cardslot%201&page="
    url = generalurl(fruitandvUrl, 20)
    return url

def dairyurl():
    dairyUrl = "https://www.allrecipes.com/recipes/17597/ingredients/dairy/?internalSource=hubcard&referringContentType=search%20results&clickId=cardslot%201&page="
    url = generalurl(dairyUrl, 20)
    return url

def pandnurl():
    pandnUrl = "https://www.allrecipes.com/recipes/95/pasta-and-noodles/?internalSource=hubcard&referringContentType=search%20results&clickId=cardslot%201&page="
    url = generalurl(pandnUrl, 25)
    return url






