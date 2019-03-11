import requests
import json
import os
import urllib.request
import timeit
import sys
baseUrl = "http://jf.luxerobot.com/"
Header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
id = sys.argv
print(id)
req = requests.get("http://jf.luxerobot.com/lesson/getLesson?pid=" + id[1] ,Header)
api = json.dumps(req.json())
api = json.loads(api)
#利用for循环下载资源
for ApiUrl in api['rows']:
    #print(ApiUrl)
    lessonUrl = baseUrl + ApiUrl['lessonUrl']
    pdfUrl = ApiUrl["pdfUrl"]
    pdfUrl = urllib.parse.quote(pdfUrl)
    pdfUrl = baseUrl + pdfUrl
    print(pdfUrl)
    title = ApiUrl['title']
    try:
         urllib.request.urlretrieve(lessonUrl, ".\Video\\" + title + ".mp4")
         print("已下载" + title)
    except:
        print("出现异常，已跳过" + title)
        pass
    try:
          urllib.request.urlretrieve(pdfUrl,".\ZipFile\\" + title + ".zip")
    except:
        print("出现异常，已跳过" + title)
        pass
    for ListUrl in ApiUrl['teachList']:
        courseid = ListUrl['id']
        courseFile = baseUrl + ListUrl['filePath']
        try:
            urllib.request.urlretrieve(courseFile,".\ZipFile\\" + title + "副本" +".zip")
            print("已下载teachList")
        except:
            print("出现异常，已跳过")

    for PlanUrl in ApiUrl["planList"]:
        getFile = PlanUrl['id']
        getName = PlanUrl['title']
        getUrl = baseUrl + PlanUrl['filePath']
        try:
            urllib.request.urlretrieve(getUrl,".\ZipFile\\" + title + getName + ".zip")
        except:
            print("出现异常以跳过")
        print("已下载planList")
