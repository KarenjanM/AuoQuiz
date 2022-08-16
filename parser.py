from abc import ABC, abstractmethod
import docx


def plain_text_parse(vocab, text):
    for row in text.split('\n'):
        if row.find('-'):
            key, value = row.split('-', 1)
            vocab[key] = value


class Parser(ABC):
    def __init__(self, path=''):
        self.path = path

    @abstractmethod
    def parse(self):
        pass


class TextParser(Parser):
    def parse(self):
        vocab = {}
        with open(self.path, 'r') as txt:
            text = txt.read()
            plain_text_parse(vocab, text)
        return vocab


class DocxParser(Parser):
    @staticmethod
    def get_text(filename):
        doc = docx.Document(filename)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)

    def parse(self):
        vocab = {}
        text = self.get_text(self.path)
        plain_text_parse(vocab, text)
        return vocab






