#encoding:utf-8
import requests
import os
import time
# 下载图片
def dowloadPic(imageUrl,filePath):
    r = requests.get(imageUrl)
    with open(filePath, "wb") as code:
        code.write(r.content)

#dowloadPic("http://1.bp.blogspot.com/_Y7rzCyUABeI/SNIltEyEnjI/AAAAAAAABOg/E1keU_52aFc/s400/ash_abhishek_365x470.jpg","1.jpg")

f = open("test.py")             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
while line:
    #print line                # 后面跟 ',' 将忽略换行符
    strs=line.split()
    if os.path.exists(strs[0]):
        print u"文件夹存在"
    else:
        os.mkdir(strs[0])

    number= int(strs[2])
    filename=strs[0]+"/"+strs[2]+".jpg"
    try:
        dowloadPic(strs[3],filename)
    except:
        line = f.readline()
        continue
    time.sleep(5)
    # print(line, end = '')　　　# 在 Python 3中使用
    line = f.readline()

f.close()

