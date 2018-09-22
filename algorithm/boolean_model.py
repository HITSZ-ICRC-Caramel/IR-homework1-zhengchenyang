import csv


class Boolean_Model():

    def __init__(self):
        self.dict = self.load_dict()  # dict, key is the word, value is the index
        self.dict_doc = self.load_dict_doc(self.dict)        # list, index represents the word index, element is the set of doc id

    def load_dict(self):
        with open("dict.txt", encoding="gbk") as f:
            dict = {}
            index = 0
            for line in f.readlines():
                words = line.split(" ")
                for word in words:

                    dict.update({word: index})
                    index = index + 1
            return dict

    def load_dict_doc(self, dict):
        dict_doc = []
        for i in range(len(dict)):
            dict_doc.append(set())
        return dict_doc


    def load_boolean_model(self):
        with open("boolean_model.csv", encoding="gbk") as f:
            reader = csv.reader(f)
            for row in reader:
                arr = [int(x) for x in row]
                word_index = arr[0]
                one_set = self.dict_doc[word_index]
                self.dict_doc[word_index] = one_set | (set(arr[1:]))

    def statistic_text(self):
        with open("doc_segmentation2.txt", encoding="gbk") as f1:
            doc_index = 0
            for line in f1.readlines():
                line = line.strip()
                line = line.strip("\n")
                words = line.split(" ")
                for word in words:
                    try:
                        word_index = self.dict[word]
                        self.dict_doc[word_index].add(doc_index)
                    except BaseException as e:
                        print(e.with_traceback())
                        print("line ", doc_index)
                        print("出现错误 ", word, word_index, " ")
                        pass
                doc_index = doc_index + 1



    def find_index_in_dict(self, word):
        return self.dict.get(word)

    def csv_persist(self):
        with open("boolean_model.csv", "w", newline='') as f:
            writer = csv.writer(f)
            for word_index in range(len(self.dict_doc)):
                row = [word_index]
                row.extend(self.dict_doc[word_index])
                writer.writerow(row)

    def search_doc(self, keys):
        word_index_dict = self.get_search_word_index_dict(keys)
        c = set()
        flag = 0
        for word_index in word_index_dict.values():
            if flag == 0:
                c = set(self.dict_doc[word_index])
            flag = flag + 1
            c = c & set(self.dict_doc[word_index])
        return c

    def get_search_word_index_dict(self, keys):
        word_index_dict = {}
        for key in keys:
            word_index = self.dict[key]
            word_index_dict.update({key: word_index})
        return word_index_dict

    def is_searched_doc(self, flag):
        for key in flag:
            if flag[key] == False:
                return False
        return True




model = Boolean_Model()
# model.statistic_text()
# model.csv_persist()
model.load_boolean_model()
print(model.search_doc(("避险","高盛")))


