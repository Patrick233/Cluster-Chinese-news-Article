# coding=utf-8
from sklearn.feature_extraction.text import CountVectorizer
import jieba
import os
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')

vectoerizer = CountVectorizer(min_df=1, max_df=1.0, token_pattern='\\b\\w+\\b')

if __name__ == '__main__':

    file = open(unicode("SportNews/1.7秒准绝杀!论科比接班人谁也别忘了这13号秀.txt", "utf8"), "r")
    doc = ""
    for line in file:
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

