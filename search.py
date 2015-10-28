#coding=utf-8
import urllib
import urllib2
import re
import fans


class NicknameSearch:
    def getNickName(self):
        nickName = raw_input("please input the nickname that you want to search:")
        return nickName
    def nick2utf8(self,name):
        params = {}
        params = {'name':name}
        name = urllib.urlencode(params)
        urlName = name.split('=')[1] 
        return urlName
    def getHomeUrl(self,text):
        regEx = re.compile(r'href=\\"http:\\/\\/weibo.com\\(/u\\)?/\d+')
        result = re.search(regEx,text)
        url=result.group(0).split('"')[1]
        url = url.replace('\\','')
        return url
    def search(self):
        nickname = self.getNickName()
        urlName = self.nick2utf8(nickname)
        url = 'http://s.weibo.com/user/'+urlName+'&Refer=index'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        text = response.read()
        #fp_raw = open("weibo.html","w+")
        #fp_raw.write(text)
        #fp_raw.close()
        homePageUrl = self.getHomeUrl(text)
        print homePageUrl
        fan = fans.Fans()
        fan.getFans(homePageUrl)
