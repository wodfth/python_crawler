from urllib.request import urlopen
import bs4

url = "http://news.naver.com/"

html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")

ul = bs_obj.find("ul", {"class":"hdline_article_list"})
# print(ul)
lis = ul.findAll("li")

# for li in lis:
#     div = li.find("div").text
#     print(div)

titles = [li.find("div").text for li in lis]

print(titles)