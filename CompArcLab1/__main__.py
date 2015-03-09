__author__ = 'vladymyr'

from CompArcLab1 import MyXmlParser
from CompArcLab1 import conf
import urllib.request

class Main:
    def main(self):
        str = conf.getUrlPath()
        xmlParser = MyXmlParser.myXMLParser(conf.getUrlPath())
        urlList = xmlParser.getDirectChildrenTagText("url")
        print(urlList)
        for url in urlList:
            file = urllib.request.urlopen(url[0])
            text = file.read()
            print("\n")
            print("read", len(text), "bytes in " + url[1])
            if (text):
                xmlParser.parseRss(text)

m = Main()
m.main()