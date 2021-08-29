from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 as p
import win32api
class info():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.chrome_driver_binary = "F:\PythonClass\chromedriver.exe"
        #self.driver=webdriver.Chrome(executable_path='F:\PythonClass\chromedriver.exe')
        self.driver = webdriver.Chrome(self.chrome_driver_binary, options=self.options)
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org/")
        search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()
        infor =self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[2]')
        readable_text=infor.text
        engine=p.init()
        engine.say(readable_text)
        engine.runAndWait()


#bot=info()
#bot.get_info("liberty bell")