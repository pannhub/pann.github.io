from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

a = [int(num) for num in input("Range : ").split()]
for i in range(a[0], a[1] + 1):
    html = urlopen("https://m.pann.nate.com/talk/c20038?order=B&gb=D&dayPage={}".format(i))
    bs = BeautifulSoup(html, "lxml")
    lst = bs.findAll("ul")[2].findAll("a")
    links = ["m.pann.nate.com" + tag.attrs["href"][:15] for tag in lst]
    tits = [tag.find("span", class_ = "tit").text.replace("\t", "").replace("\n", "") for tag in lst]
    for i in range(len(links)):
        print("{0} {1}".format(links[i], tits[i]))
        
