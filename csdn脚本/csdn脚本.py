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

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    # 伪装成Chrome浏览器
refererData = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=csdn%20%E6%80%9D%E6%83%B3%E7%9A%84%E9%AB%98%E5%BA%A6%20csdnzouqi&oq=csdn%20%E6%80%9D%E6%83%B3%E7%9A%84%E9%AB%98%E5%BA%A6&rsv_pq=fe7241c2000121eb&rsv_t=0dfaTIzsy%2BB%2Bh4tkKd6GtRbwj3Cp5KVva8QYLdRbzIz1CCeC1tOLcNDWcO8&rqlang=cn&rsv_enter=1&rsv_sug3=11&rsv_sug2=0&inputT=3473&rsv_sug4=3753'    # 伪装成是从baidu.com搜索到的文章
data = ''    # 将GET方法中待发送的数据设置为空
headers = {'User-Agent' : user_agent, 'Referer' : refererData}    # 构造GET方法中的Header
count = 0    # 初始化计数器
request = urllib.request.Request(url,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request = urllib.request.Request(url2,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request = urllib.request.Request(url3,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request = urllib.request.Request(url4,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)   
request = urllib.request.Request(url5,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request = urllib.request.Request(url6,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)   
request = urllib.request.Request(url7,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request = urllib.request.Request(url8,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)   
request = urllib.request.Request(url9,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)    
request = urllib.request.Request(url10,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url11,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url12,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url13,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url14,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url15,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url16,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url17,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url18,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url19,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url20,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url21,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  
request = urllib.request.Request(url22,  data=urllib.parse.urlencode(data).encode(encoding='UTF8'), headers=headers)  





while 1:    # 一旦开刷就停不下来
    rec = urllib.request.urlopen(request)  # 发送GET请求，获取博客文章页面资源
    page = rec.read()    # 读取页面内容到内存中的变量，这句代码可以不要
    count += 1    # 计数器加
    print(count)    # 打印当前循环次数
    if count % 6:    # 每6次访问为1个循环，其中5次访问等待时间为31秒，另1次为61秒
        time.sleep(31)    # 为每次页面访问设置等待时间是必须的，过于频繁的访问会让服务器发现刷阅读量的猥琐行为并停止累计阅读次数
    else:
        time.sleep(61)
print(page)    # 打印页面信息，这句代码永远不会执行
