import jieba
import re

def segmentation(filename):
    # load stop words
    stop_words = []
    with open("stopwords.dat", encoding="utf-8") as f1:
        for line in f1.readlines():
            stop_words.append(line.strip())
        stop_words.append(" ")
    # segmentation
    with open("doc_segmentation.txt", "w") as f2:
        with open(filename, encoding="utf-8") as f3:
            str = ""
            flag = 0
            for line in f3.readlines():
                word_list = list(jieba.cut(line, cut_all=False))
                for word in word_list:
                    if word not in stop_words:
                        str = str + word.strip() + " "
                str = str + "\n"
                flag = flag + 1
                if flag == 1000:
                    print(flag)
                f2.write(str)
                str = ""


def segmentation2(input_file, output_file):
    with open(input_file, encoding='gbk') as f1:
        with open(output_file, "w") as f2:
            for line in f1.readlines():
                words = line.split(" ")
                for i in range(len(words)-1, -1, -1):
                    if isDigit(words[i]):
                        words.pop(i)
                    elif year_month_day(words[i]):
                        words.pop(i)
                str = ""
                for i in range(len(words)):
                    str = str + words[i] + " "
                f2.write(str)

def isDigit(str):
    matchObj = re.search(r'[-+]?[0-9]+[\.]?[0-9]*', str)
    if matchObj==None:
        return False
    else:
        return True

def year_month_day(str):
    if str=="年":
        return True
    elif str=="月":
        return True
    elif str=="日":
        return True
    else:
        return False



# segmentation("news_retrieval.csv")
segmentation2("doc_segmentation.txt", "doc_segmentation2.txt")



