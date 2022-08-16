from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


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
            password_field.send_keys(self.password)
            password_field.send_keys(Keys.ENTER)
        except Exception:
            print('Invalid login information')
        finally:
            self.driver.quit()


user = User()
