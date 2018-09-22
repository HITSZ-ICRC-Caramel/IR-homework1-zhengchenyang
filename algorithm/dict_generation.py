
def dict_generation():
    dict_set = set()
    with open("doc_segmentation2.txt", encoding="gbk") as f:
        for line in f.readlines():
            words = line.split(" ")
            for word in words:
                dict_set.add(word)

    print(len(dict_set))
    with open("dict.txt", "w") as f1:
        str = ""
        for word in dict_set:
            str = str + word + " "
        f1.write(str)

dict_generation()