from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from parser import TextParser, DocxParser, plain_text_parse


class Vocabulary:
    def __init__(self, data_type):
        self.vocab = {}
        self.data_type = data_type

    def get_vocab(self, path, text=''):
        if self.data_type == 'docx':
            parser = DocxParser(path)
        elif self.data_type == 'txt':
            parser = TextParser(path)
        else:
            parser = plain_text_parse(self.vocab, text)
        self.vocab = parser.parse()


class User:
    def __init__(self, *args, **kwargs):
        self.username = kwargs.get('username', args[0])
        self.password = kwargs.get('password', args[1])
        self.driver = webdriver.Chrome(kwargs.get('driver', args[2]))

    def login(self):
        try:
            self.driver.get('https://quizlet.com/login')
            username_field = self.driver.find_element(By.NAME, 'username')
            password_field = self.driver.find_element(By.NAME, 'password')
            username_field.send_keys(self.username)
            sleep(4)
            password_field.send_keys(self.password)
            sleep(4)
            password_field.send_keys(Keys.ENTER)
            sleep(5)
        except Exception:
            print('Invalid login information')
        finally:
            self.driver.quit()

user = User('karenjantv@gmail.com', 'Karenjan2004',
            'C:\\Users\\karen\\Desktop\\MyDjangoApps\\AutoQuiz\\chromedriver.exe')
user.login()
