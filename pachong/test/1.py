import re
import urllib
 
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
 
def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x = x + 1
    
    
html = getHtml("http://news.whsw.net/?viewnews-8295")
getImg(html)
