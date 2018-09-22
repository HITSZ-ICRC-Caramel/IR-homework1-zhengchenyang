class Doc(object):

    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.true_word_list = []


    def add_word_index(self, word_index):
        self.true_word_list.append(word_index)


class Boolean_Model():

    def __init__(self):
        self.dict = self.load_dict()
        self.docs = {}

    def load_dict(self):
        with open("dict.txt", encoding="gbk") as f:
            dict = []
            line = f.readline()
            words = line.split(" ")
            for word in words:
                dict.append(word)
            return dict

    def statistic_text(self):
        with open("doc_segmentation2.txt", encoding="gbk") as f1:
            doc_id = 0
            for line in f1.readlines():
                words = line.split(" ")
                doc = Doc(doc_id)
                for word in words:
                    word_index = find_index_in_dict(word)
                    doc.add_word_index(word_index)
                doc_id = doc_id + 1

    def find_index_in_dict(self, word):
