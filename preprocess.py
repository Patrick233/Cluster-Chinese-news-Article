# coding=utf-8
from sklearn.feature_extraction.text import CountVectorizer
import jieba
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def pre_process(file_name):
    file = open(unicode(file_name, "utf8"), "r")
    doc = ""
    for line in file:
        
        re.sub(r'[^\w]', '', line)
        line = line.replace(" ", "")
        doc += line

    seg_list = jieba.cut(doc, cut_all=False)
    content = " ".join(seg_list)
    print("Default Mode: " + content)  # 精确模式

    try:
        with open('testBags.txt', 'w') as file_object:
            # content = content.encode('ascii', 'ignore').decode('ascii')
            # print (content)
            file_object.write(content)
            file_object.close()
    except Exception, e:
        print (e)
