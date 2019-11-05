from selenium import webdriver
import requests


class Douyuspider:
    def __init__(self) -> None:
        self.start_url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def run(self):
        # start_url
        url = ''
