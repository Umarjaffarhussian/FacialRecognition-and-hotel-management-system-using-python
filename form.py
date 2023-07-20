from selenium import webdriver
from selenium.webdriver.common.by import By
import time

web = webdriver.Chrome(executable_path="C:\\Users\\ELCOT\\Downloads\\chromedriver.exe")
web.get('https://docs.google.com/forms/d/e/1FAIpQLSe8ci6dfMCAWD9q6zcVBGwyTOl7hqcIEEhpWeDuYHDWUANtOQ/viewform?usp=sf_link')

web.maximize_window() # For maximizing window
web.implicitly_wait(20)
time.sleep(2)

Name = "jaffer"
last = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(Name)

Mail = "9920116011@klu.ac.in"
last = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(Mail)

Address = "213,seethakathi street"
last = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
last.send_keys(Address)

Phonenumber = "7871485567"
last = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(Phonenumber)

Submit = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
Submit.click()


