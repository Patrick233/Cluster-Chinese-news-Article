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

    dest = "/Users/Patrizio/Desktop/neu/cs6220/project/after_process/{}".format(idx)
    print (dest)
    with open(unicode(dest, "utf8"), "w") as filehandle:
        lines = filter(lambda x: x.strip(), doc)
        filehandle.writelines(lines)
        filehandle.close


if __name__ == '__main__':
    # print (ignore_set)
    dir_name = "/Users/Patrizio/Desktop/neu/cs6220/project/news/"
    count_topic = 0
    for dir in os.listdir(dir_name):
        print (dir)
        if dir.find(".DS") == -1:
            print (dir)
            count_topic += 1
            count_file = 1
            sub_dir = dir_name+dir
            for file in os.listdir(sub_dir):
                file_name = "{}/{}".format(sub_dir, file)
                print (file_name)
                if os.path.getsize(file_name) > 100 and os.path.isfile(file_name) and file_name.find(".txt") != -1:
                    print (file_name)
                    count_file +=1
                    pre_process(file, sub_dir, count_topic*10000+count_file)