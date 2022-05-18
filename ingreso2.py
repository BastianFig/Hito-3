from selenium import webdriver
import time


correo = "bastyanfigueroa1@gmail.com"


driver = webdriver.Edge(executable_path=r"C:\drivers\msedgedriver.exe")
driver.get("https://stickershop.cl/account/login")

time.sleep(10)
nom = driver.find_element_by_xpath('//*[@id="customer_login"]/a[1]').click()

nom = driver.find_element_by_xpath('//*[@id="RecoverEmail"]')
nom.send_keys(correo) #pone correo


nom = driver.find_element_by_xpath('//*[@id="MainContent"]/div/div[1]/form/button').click()
time.sleep(20)
driver.close()
