#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def bForce():
	driver = webdriver.Edge(executable_path=r"C:\drivers\msedgedriver.exe")
    driver.get("https://www.fide.cl/")
    nom = driver.find_element_by_xpath('//*[@id="menu-item-5520"]').click()
	
	for i in range(59, 90):
		user = driver.find_element_by_xpath("//*[@id=\"user_email\"]")
		user.send_keys("rr"+str(i)+"@rrr.com")
		password = driver.find_element_by_xpath("//*[@id=\"user_password\"]")
		password.send_keys("12345678")
		pass_confirm = driver.find_element_by_xpath("//*[@id=\"user_password_confirmation\"]")
		pass_confirm.send_keys("12345678")
		driver.find_element_by_name("commit").click()
		close = driver.find_element_by_xpath("/html/body/li/a")
		close.click()
		driver.get("https://www.fide.cl/")
	driver.close()
bForce()