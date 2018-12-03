from bs4 import BeautifulSoup
import requests

html = requests.get("https://blog.csdn.net/z_xiaoxin/article/details/82051982").text
bs = BeautifulSoup(html)
temp  = bs.find(name="div")
print(temp)
