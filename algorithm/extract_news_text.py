from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def __init__(self):
        self.flag = False
        self.out_file = open("news_text.txt", "a+", encoding="utf-8")

    def start_element(self, name, attrs):

        if name == 'content':
            self.flag = True
        else:
            self.flag = False

    def end_element(self, name):
        pass

    def char_data(self, text):
        if self.flag == True:
            self.flag = False
            if text != "" and text != "\n":
                self.out_file.write(text+"\n")


def load_xml(filename):
    xml = ""
    with open(filename, encoding="utf-8") as f:
        xml = f.read()
    parse_xml(xml)

def parse_xml(xml):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)


def extract_news_text(filename):
    load_xml(filename)
    pass

extract_news_text("news_sohusite_xml.smarty.dat")

