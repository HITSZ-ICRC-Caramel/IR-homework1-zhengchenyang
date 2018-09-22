
def dict_generation():
    dict_set = set()
    with open("doc_segmentation2.txt", encoding="gbk") as f:
        for line in f.readlines():
            words = line.split(" ")
            for word in words:
                dict_set.add(word)
                if len(dict_set)%100 == 0:
                    print(len(dict_set))

    with open("dict.txt", "w") as f1:
        str = ""
        i = 1
        for word in dict_set:
            str = str + word + " "
            if i % 100 == 0:
                f1.write(str)
                str = ""
            i = i + 1

        f1.write(str)

dict_generation()