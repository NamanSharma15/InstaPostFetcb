import pandas as pd
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class ProfileDetails:
    def __init__(self,url):
        if("www.instagram.com/" not in url):
            url = "https://www.instagram.com/"+url
        self.data = {}
        self.url = url
        self.getHtml()
        self.getFollowAndPosts()
        self.getProfile()
        self.getPosts()
    def getHtml(self)->None:
        # options = webdriver.ChromeOptions() 
        # options.add_experimental_option("detach", True)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless') 
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.url)
        time.sleep(5)
        htmlSource = self.driver.page_source
        self.html = BeautifulSoup(htmlSource, 'html.parser')
    def getProfile(self):
        xdata = self.html.find("h2",class_="x1lliihq")
        self.data["User Id"] = xdata.text
    def getFollowAndPosts(self):
        xdata = self.html.find_all("li",class_="xl565be")
        self.data["Post Count"] = xdata[0].text
        self.data["Followers"] = xdata[1].text
        self.data["Following"] = xdata[2].text
        print(self.data)
    def getPosts(self):
        posts = self.html.find_all("a",class_="xjbqb8w")
        print(posts[0]["href"])
ProfileDetails("yoyohoneysingh")
