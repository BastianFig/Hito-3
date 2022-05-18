from selenium import webdriver
import time

correo = "Elreydelvalo@gmail.com"
contraseña = "bebesita"

driver = webdriver.Edge(executable_path=r"C:\drivers\msedgedriver.exe")
driver.get("https://stickershop.cl/account/login")

time.sleep(20)

nom = driver.find_element_by_xpath('//*[@id="CustomerEmail"]')
nom.send_keys(correo) #pone correo
nom = driver.find_element_by_xpath('//*[@id="CustomerPassword"]')
nom.send_keys(contraseña) #pone contraseña
nom = driver.find_element_by_xpath('//*[@id="customer_login"]/button').click()
time.sleep(10)
driver.close()