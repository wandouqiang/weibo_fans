#coding=utf-8
import urllib
import urllib2
import re


class Fans:
    def getPageText(self,url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        text = response.read()
        return text
    def getFansUrl(self,text):
        regEx = re.compile(r"\$CONFIG\['page_id'\]='(\d+)'")      
        num = re.search(regEx,text).group(1)

        fansUrl = []
        for pageNum in range(6):
            fansUrl.append("http://weibo.com/p/"+num+"/follow?relate=fans&page="+str(pageNum)+"#Pl_Official_HisRelation__62")
        return fansUrl
        
    def getFansNick(self,text):
        reg = re.compile(r'\\"uid=(\d+?)&fnick=(.+?)&sex')
        result = re.findall(reg,text)
        nickList = list(set(result))
        for i in nickList:
            print i[0],i[1]
        return nickList   #for((ID,nick),(ID,nick))
    
    def getFans(self,homeUrl):
        homepage = self.getPageText(homeUrl)
        fansUrl = self.getFansUrl(homepage)
        fansNick = []
        for url in fansUrl: 
            
            fanspage = self.getPageText(url)
            fansNick.extend(self.getFansNick(fanspage))
        for i in fansNick:
            print i[0],i[1]
        print len(fansNick)
