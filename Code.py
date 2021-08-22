
import os
import sys
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
class twitterbot:
    def __init__(self,username,password):
        #username and password
        self.username=username
        self.password=password

        #platform
        if  sys.platform=="linux":
            driver_path=os.path.join(os.getcwd(),"chromedriver")
        elif sys.platform.startswith("win"):
            driver_path=os.path.join(os.getcwd(),"chromedriver.exe")
        
        #chrome driver for chrome control
        self.driver=webdriver.Chrome(executable_path=driver_path)

    def login(self):
        #url for twitter
        url="https://twitter.com/login"
        self.driver.get(url)
        time.sleep(3)

        #username, password field and login button
        username_field=self.driver.find_element(By.NAME,"session[username_or_email]")
        password_field=self.driver.find_element(By.NAME,"session[password]")
        login_button=self.driver.find_element(By.XPATH,'//div[@role="button"]')

        #fill the username and password blank and click login button
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        login_button.click()
        
def main(username,password):
   bot=twitterbot(username,password)
   bot.login()
   time.sleep(5)

if __name__=="__main__":
    username=input("Enter your username:")
    password=getpass.getpass("Enter your password")
    main(username,password)