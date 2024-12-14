import pandas as pd
from bs4 import BeautifulSoup 
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
class InstagramPost:
    def __init__(self,url):
        self.url:str = url
        self.data:dict = {}
        self.insta_url= "https://www.instagram.com/"
        self._getHtml()
        self._setSource()
        self._setProfile()
        self._setLikes()
        self._setComments()
        self._getProfileUrl()
    def _getProfileUrl(self):
        self.data["profile_url"] = self.insta_url+self.data["profile_name"]
    def getData(self)->dict:
        return self.data
    def _getHtml(self)->None:
        options = webdriver.ChromeOptions() 
        options.add_argument('--headless') 
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        time.sleep(5)
        htmlSource = driver.page_source
        self.html = BeautifulSoup(htmlSource, 'html.parser')
    def _setSource(self)->None:
        self.data["source"] = ""
        post_div = self.html.find("div",class_="_aatk")
        post_div1 = self.html.findAll("div",class_="x1uhb9sk")
        try:
            self.data["source"]= str(post_div.find("video")['src'])
        except:
            pass
        try:
            self.data["source"]= str(post_div1.find("video")['src'])
        except:
            pass
        try:
            self.data["source"]= str(post_div.find("img")["src"])
        except:
            pass
        try:
            self.data["source"]= str(post_div1.find("img")["src"])
        except:
            pass
    def _setProfile(self)->None:
        self.data["profile_name"] =""
        profile_div = self.html.find("header",class_="_aaqw")
        try:
            self.data["profile_name"] = str(profile_div.text).split("•")[0].replace("Verified","")
        except:
            pass
    def _setLikes(self)->None:
        self.data["likes"]= 0
        likes_div = self.html.find("section",class_="_ae5m")
        try:
            self.data["likes"] = int(str(likes_div.text).replace(",","").split(" ")[0])
        except:
            pass
    def _setComments(self)->None:
        self.data["comments"] = []
        comments_div = self.html.findAll("a",class_="x568u83")
        comments_span = self.html.findAll("span",class_="_aacu")
        user = [i.text for i in comments_div]
        comment = [i.text for i in comments_span]
        result = []
        for i,j in zip(user,comment):
            result.append({f"{i}":j})
        self.data["comments"] = result
if __name__ == "__main__":  
    x = InstagramPost()