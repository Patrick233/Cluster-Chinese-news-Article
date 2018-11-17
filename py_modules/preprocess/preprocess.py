# coding=utf-8
from sklearn.feature_extraction.text import CountVectorizer
import jieba
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

ignore_set = {1}
with open("../../symbols.txt") as ignores:
    for line in ignores:
        ignore_set.add(line)


def pre_process(file, dir_name):
    file_name = "{}/{}".format(dir_name, file)
    f = open(unicode(file_name, "utf8"), "r")
    doc = ""
    for line in f:
        line = line.decode("utf8")
        result = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"), line)
        result = re.sub(r'[0-9]+', '', result)
        result = result.replace(" ", "")
        doc += result

    dest = dir_name + "/after_process/" + file
    print (dest)
    with open(unicode(dest, "utf8"), "w") as filehandle:
        lines = filter(lambda x: x.strip(), doc)
        filehandle.writelines(lines)
        filehandle.close


if __name__ == '__main__':
    # print (ignore_set)
    dir_name = "/Users/Patrizio/Desktop/neu/cs6220/project/news/test_sport/"
    for file in os.listdir(dir_name):
        file_name = "{}/{}".format(dir_name, file)
        print (file_name)
        if os.path.getsize(file_name) > 100 and os.path.isfile(file_name) and file_name.find(".txt") != -1:
            print (file_name)
            pre_process(file, dir_name)