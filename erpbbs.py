#! /usr/bin/python

'''
Python Script for scrapping CGPA from ERP IITBBS
'''

__author__ = 'Aman Pratap Singh'
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

roll = raw_input('Roll Number: ')
password = getpass.getpass()

chrome = webdriver.Chrome()
chrome.set_window_position(0, 0)
chrome.get("http://webapps.iitbbs.ac.in/rerp/")
rl = chrome.find_element_by_name("email")
pw = chrome.find_element_by_name("password")
rl.send_keys(roll)
pw.send_keys(password)
pw.send_keys(Keys.RETURN)	
chrome.find_element_by_link_text('RESULT').click()
cg = chrome.find_element_by_xpath('//*[@id="content"]/div/div[3]/table/tbody/tr[2]/td/bt/table[3]/tbody/tr/td[2]/b')
print '\n' + cg.text
chrome.close()
