# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 21:16:44 2022

@author: Everton SSD

https://selenium-python.readthedocs.io/locating-elements.html
"""
from app import Chrome_Auto

chrome = Chrome_Auto()
chrome.acessa('https://www.google.com/')
chrome.inputs()
#chrome.sai()