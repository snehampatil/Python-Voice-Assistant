from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 as p
import win32api


class Movie():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.chrome_driver_binary = "F:\PythonClass\chromedriver.exe"
        # self.driver=webdriver.Chrome(executable_path='F:\PythonClass\chromedriver.exe')
        self.driver = webdriver.Chrome(self.chrome_driver_binary, options=self.options)

    def movie_review(self, name):
        self.driver.get("https://www.google.com")
        search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(name + " movie reviews")
        submit = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
        self.driver.execute_script("arguments[0].click();", submit)
        #submit.click()


#bot = Movie()
#bot.movie_review("spirited away")
