from selenium import webdriver
import time



nombre = "Sebarex"
apellido = "Riquelmis"
correo = "Elreydelvalo@gmail.com"
contraseña = "bebesita"


driver = webdriver.Edge(executable_path=r"C:\drivers\msedgedriver.exe")
driver.get("https://stickershop.cl/account/register")

time.sleep(20)

nom = driver.find_element_by_xpath('//*[@id="RegisterForm-FirstName"]')
nom.send_keys(nombre) #pone nombre
nom = driver.find_element_by_xpath('//*[@id="RegisterForm-LastName"]')
nom.send_keys(apellido) #pone apellido
nom = driver.find_element_by_xpath('//*[@id="RegisterForm-email"]')
nom.send_keys(correo) #pone correo
nom = driver.find_element_by_xpath('//*[@id="RegisterForm-password"]')
nom.send_keys(contraseña) #pone contraseña
nom = driver.find_element_by_xpath('//*[@id="create_customer"]/button').click()
time.sleep(10)
driver.close()




