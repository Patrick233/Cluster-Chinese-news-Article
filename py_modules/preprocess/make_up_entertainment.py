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


def pre_process(file, dir_name, idx):
    file_name = "{}/{}".format(dir_name, file)
    f = open(unicode(file_name, "utf8"), "r")
    doc = ""
    for line in f:
        line = line.decode("utf8")
        result = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"), line)
        result = re.sub(r'[0-9]+', '', result)
        result = result.replace(" ", "")
        doc += result

    dest = "/Users/Patrizio/Desktop/neu/cs6220/project/make_up_entertain/{}".format(idx)
    print (dest)
    with open(unicode(dest, "utf8"), "w") as filehandle:
        lines = filter(lambda x: x.strip(), doc)
        filehandle.writelines(lines)
        filehandle.close


if __name__ == '__main__':
    # print (ignore_set)
    dir_name = "/Users/Patrizio/Desktop/neu/cs6220/project/news/entertainment"
    count_topic = 0
    # for dir in os.listdir(dir_name):
    #     print (dir)
    #     if dir.find(".DS") == -1:
    #         print (dir)
    #         count_topic += 1
    #         count_file = 1
    #         sub_dir = dir_name+dir

    # 1: Sport 2: Health 3: Education 4: Fansion 5: Entertainment 6:Tech
    count_file = 50000
    for file in os.listdir(dir_name):
        file_name = "{}/{}".format(dir_name, file)
        print (file_name)
        if os.path.getsize(file_name) > 100 and os.path.isfile(file_name) and file_name.find(".txt") != -1:
            print (file_name)
            count_file += 1
            pre_process(file, dir_name, count_topic * 10000 + count_file)
