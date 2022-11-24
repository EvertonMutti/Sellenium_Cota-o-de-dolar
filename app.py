# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:42:20 2022

@author: Everton SSD
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

class Chrome_Auto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('user-data-dir=Perfil')
        #Setando o perfil de usuario do chrome
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options = self.options
            )
    def acessa(self, site):
        self.chrome.get(site)
        
    def sai(self):
        self.chrome.quit()
    
    def inputs(self):
        _input = self.chrome.find_element(By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
        _input.send_keys('Cotação do dólar')
        button = self.chrome.find_element(By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b')
        button.click()
        
        
        

if __name__ == '__main__':
    chrome = Chrome_Auto()