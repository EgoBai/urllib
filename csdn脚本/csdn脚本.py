#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib    # Python中的cURL库
import urllib.request
import time    # 时间函数库，包含休眠函数sleep()
url = 'https://blog.csdn.net/ego_bai/article/details/80872730'    
url2 = 'https://blog.csdn.net/ego_bai/article/details/80873242'   
url3 = 'https://blog.csdn.net/ego_bai/article/details/79866112'   
url4 = 'https://blog.csdn.net/ego_bai/article/details/79827195'   
url5 = 'https://blog.csdn.net/ego_bai/article/details/78332083'   
url6 = 'https://blog.csdn.net/ego_bai/article/details/81004240'   
url7 = 'https://blog.csdn.net/ego_bai/article/details/81002966'   
url8 = 'https://blog.csdn.net/ego_bai/article/details/80827191'   
url9 = 'https://blog.csdn.net/ego_bai/article/details/80656683'   
url10 = 'https://blog.csdn.net/ego_bai/article/details/80644312'  
url11 = 'https://blog.csdn.net/ego_bai/article/details/80644256'  
url12 = 'https://blog.csdn.net/ego_bai/article/details/80635306'  
url13= 'https://blog.csdn.net/ego_bai/article/details/80635298'   
url14 = 'https://blog.csdn.net/ego_bai/article/details/80634516'  
url15 = 'https://blog.csdn.net/ego_bai/article/details/80615277'  
url16= 'https://blog.csdn.net/ego_bai/article/details/80611225'   
url17 = 'https://blog.csdn.net/ego_bai/article/details/80610830'  
url18 = 'https://blog.csdn.net/ego_bai/article/details/80570228'  
url19 = 'https://blog.csdn.net/ego_bai/article/details/80567958'  
url20 = 'https://blog.csdn.net/ego_bai/article/details/79882079'  
url21 = 'https://blog.csdn.net/ego_bai/article/details/80293632'  
url22 = 'https://blog.csdn.net/ego_bai/article/details/79866651' 

url23 = 'https://blog.csdn.net/ego_bai/article/details/80615365' 
url24 = 'https://blog.csdn.net/ego_bai/article/details/80560894' 
url25 = 'https://blog.csdn.net/ego_bai/article/details/80560872' 
url26 = 'https://blog.csdn.net/ego_bai/article/details/80560068' 
url27 = 'https://blog.csdn.net/ego_bai/article/details/80559907' 
url28 = 'https://blog.csdn.net/ego_bai/article/details/80546965' 
url29 = 'https://blog.csdn.net/ego_bai/article/details/80546916' 
url30 = 'https://blog.csdn.net/ego_bai/article/details/80522512' 
url31 = 'https://blog.csdn.net/ego_bai/article/details/80521657' 
url32 = 'https://blog.csdn.net/ego_bai/article/details/80508122' 
url33 = 'https://blog.csdn.net/ego_bai/article/details/80505890' 
url34 = 'https://blog.csdn.net/ego_bai/article/details/80481687' 
url35 = 'https://blog.csdn.net/ego_bai/article/details/80481262' 
url36 = 'https://blog.csdn.net/ego_bai/article/details/80461304' 
url37 = 'https://blog.csdn.net/ego_bai/article/details/80460854' 
url38 = 'https://blog.csdn.net/ego_bai/article/details/80442524' 
url39 = 'https://blog.csdn.net/ego_bai/article/details/80441529' 
url40 = 'https://blog.csdn.net/ego_bai/article/details/80441474' 
url41 = 'https://blog.csdn.net/ego_bai/article/details/80206524' 
url42 = 'https://blog.csdn.net/ego_bai/article/details/79780128' 
url43 = 'https://blog.csdn.net/ego_bai/article/details/79689617' 
url44 = 'https://blog.csdn.net/ego_bai/article/details/79643447' 
url45 = 'https://blog.csdn.net/ego_bai/article/details/79633694' 
url46 = 'https://blog.csdn.net/ego_bai/article/details/79633556' 
url47 = 'https://blog.csdn.net/ego_bai/article/details/79602006' 
url48 = 'https://blog.csdn.net/ego_bai/article/details/79587401' 
url49 = 'https://blog.csdn.net/ego_bai/article/details/78663841' 
url50 = 'https://blog.csdn.net/ego_bai/article/details/78528247' 
url51 = 'https://blog.csdn.net/ego_bai/article/details/78262130'
url52 = 'https://blog.csdn.net/ego_bai/article/details/78262043'
url53 = 'https://blog.csdn.net/ego_bai/article/details/78261977'
url54 = 'https://blog.csdn.net/ego_bai/article/details/78066049'
url55 = 'https://blog.csdn.net/ego_bai/article/details/76229064'
url56 = 'https://blog.csdn.net/ego_bai/article/details/76223676'
url57 = 'https://blog.csdn.net/ego_bai/article/details/72846843'
url58 = 'https://blog.csdn.net/ego_bai/article/details/75434691'
url59 = 'https://blog.csdn.net/ego_bai/article/details/54848516'
url60 = 'https://blog.csdn.net/ego_bai/article/details/54848205'
url61 = 'https://blog.csdn.net/ego_bai/article/details/54099206'
url62 = 'https://blog.csdn.net/ego_bai/article/details/53930623'
url63 = 'https://blog.csdn.net/ego_bai/article/details/53930388'
url63 = 'https://blog.csdn.net/ego_bai/article/details/53930357'
url63 = 'https://blog.csdn.net/ego_bai/article/details/53930101'
url63 = 'https://blog.csdn.net/ego_bai/article/details/53930049'
url63 = 'https://blog.csdn.net/ego_bai/article/details/53929833'
url64 = 'https://blog.csdn.net/ego_bai/article/details/53929664'
url65 = 'https://blog.csdn.net/ego_bai/article/details/80615365'


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    # 伪装成Chrome浏览器
refererData = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=csdn%20%E6%80%9D%E6%83%B3%E7%9A%84%E9%AB%98%E5%BA%A6%20csdnzouqi&oq=csdn%20%E6%80%9D%E6%83%B3%E7%9A%84%E9%AB%98%E5%BA%A6&rsv_pq=fe7241c2000121eb&rsv_t=0dfaTIzsy%2BB%2Bh4tkKd6GtRbwj3Cp5KVva8QYLdRbzIz1CCeC1tOLcNDWcO8&rqlang=cn&rsv_enter=1&rsv_sug3=11&rsv_sug2=0&inputT=3473&rsv_sug4=3753'    # 伪装成是从baidu.com搜索到的文章
data = ''    # 将GET方法中待发送的数据设置为空
headers = {'User-Agent' : user_agent, 'Referer' : refererData}    # 构造GET方法中的Header
count = 0    # 初始化计数器
request = urllib.request.Request(url,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request2 = urllib.request.Request(url2,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request3 = urllib.request.Request(url3,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request4 = urllib.request.Request(url4,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)   
request5 = urllib.request.Request(url5,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request6 = urllib.request.Request(url6,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)   
request7 = urllib.request.Request(url7,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request8 = urllib.request.Request(url8,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)   
request9 = urllib.request.Request(url9,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request10 = urllib.request.Request(url10,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request11 = urllib.request.Request(url11,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request12 = urllib.request.Request(url12,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request13 = urllib.request.Request(url13,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request14 = urllib.request.Request(url14,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request15 = urllib.request.Request(url15,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request16 = urllib.request.Request(url16,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request17 = urllib.request.Request(url17,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request18 = urllib.request.Request(url18,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request19 = urllib.request.Request(url19,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request20 = urllib.request.Request(url20,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request21 = urllib.request.Request(url21,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request22 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request23 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request24 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request25 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request26 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request27 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request28 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request29 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request30 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request31 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request32 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request33 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request34 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request35 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request36 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request37 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request38 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request39 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request40 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request41 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request42 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request43 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request44 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request45 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request46 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request47 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request48 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request49 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request50 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request51 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request52 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request53 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request54 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request55 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request56 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request57 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request58 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request59 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request60 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request61 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request62 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request63 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request64 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request65 = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  

while 1:    # 一旦开刷就停不下来
    rec = urllib.request.urlopen(request)  # 发送GET请求，获取博客文章页面资源
    rec2 = urllib.request.urlopen(request2)
    rec3 = urllib.request.urlopen(request3)
    rec4 = urllib.request.urlopen(request4)
    rec5 = urllib.request.urlopen(request5)
    rec6 = urllib.request.urlopen(request6)
    rec7 = urllib.request.urlopen(request7)
    rec8 = urllib.request.urlopen(request8)
    rec9 = urllib.request.urlopen(request9)
    rec10 = urllib.request.urlopen(request10)
    rec11 = urllib.request.urlopen(request11)
    rec12 = urllib.request.urlopen(request12)
    rec13 = urllib.request.urlopen(request13)
    rec14 = urllib.request.urlopen(request14)
    rec15 = urllib.request.urlopen(request15)
    rec16 = urllib.request.urlopen(request16)
    rec17 = urllib.request.urlopen(request17)
    rec18 = urllib.request.urlopen(request18)
    rec19 = urllib.request.urlopen(request19)
    rec20 = urllib.request.urlopen(request20)
    rec21 = urllib.request.urlopen(request21)
    rec22 = urllib.request.urlopen(request22)
    rec23 = urllib.request.urlopen(request23)
    rec24 = urllib.request.urlopen(request24)
    rec25 = urllib.request.urlopen(request25)
    rec26 = urllib.request.urlopen(request26)
    rec27 = urllib.request.urlopen(request27)
    rec28 = urllib.request.urlopen(request28)
    rec29 = urllib.request.urlopen(request29)
    rec30 = urllib.request.urlopen(request30)
    rec31 = urllib.request.urlopen(request31)
    rec32 = urllib.request.urlopen(request32)
    rec33 = urllib.request.urlopen(request33)
    rec34 = urllib.request.urlopen(request34)
    rec35 = urllib.request.urlopen(request35)
    rec36 = urllib.request.urlopen(request36)
    rec37 = urllib.request.urlopen(request37)
    rec38 = urllib.request.urlopen(request38)
    rec39 = urllib.request.urlopen(request39)
    rec40 = urllib.request.urlopen(request40)
    rec41 = urllib.request.urlopen(request41)
    rec42 = urllib.request.urlopen(request42)
    rec43 = urllib.request.urlopen(request43)
    rec44 = urllib.request.urlopen(request44)
    rec45 = urllib.request.urlopen(request45)
    rec46 = urllib.request.urlopen(request46)
    rec47 = urllib.request.urlopen(request47)
    rec48 = urllib.request.urlopen(request48)
    rec49 = urllib.request.urlopen(request49)
    rec50 = urllib.request.urlopen(request50)
    rec51 = urllib.request.urlopen(request51)
    rec52 = urllib.request.urlopen(request52)
    rec53 = urllib.request.urlopen(request53)
    rec53 = urllib.request.urlopen(request54)
    rec55 = urllib.request.urlopen(request55)
    rec56 = urllib.request.urlopen(request56)
    rec57 = urllib.request.urlopen(request57)
    rec58 = urllib.request.urlopen(request58)
    rec59 = urllib.request.urlopen(request59)
    rec60 = urllib.request.urlopen(request60)
    rec61 = urllib.request.urlopen(request61)
    rec62 = urllib.request.urlopen(request62)
    rec63 = urllib.request.urlopen(request63)
    rec64 = urllib.request.urlopen(request64)
    rec65 = urllib.request.urlopen(request65)

    count += 1    # 计数器加
    print(count)    # 打印当前循环次数
    if count % 6:    # 每6次访问为1个循环，其中5次访问等待时间为31秒，另1次为61秒
        time.sleep(31)    # 为每次页面访问设置等待时间是必须的，过于频繁的访问会让服务器发现刷阅读量的猥琐行为并停止累计阅读次数
    else:
        time.sleep(61)
print(page)    # 打印页面信息，这句代码永远不会执行
