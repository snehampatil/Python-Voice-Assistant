from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 as p
import win32api


class Song():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.chrome_driver_binary = "F:\PythonClass\chromedriver.exe"
        # self.driver=webdriver.Chrome(executable_path='F:\PythonClass\chromedriver.exe')
        self.driver = webdriver.Chrome(self.chrome_driver_binary, options=self.options)

    def play(self, name):
        self.name=name
        self.driver.get(url="https://www.youtube.com/results?search_query="+name)
        search = self.driver.find_element_by_xpath('//*[@id="search"]')
        self.driver.execute_script("arguments[0].click();", search)
        #search.click()

        #submit.click()


#bot = Song()
#bot.play("spirited away")
