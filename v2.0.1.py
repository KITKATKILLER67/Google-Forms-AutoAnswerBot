import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

while True:

	driver = webdriver.Chrome()

	driver.get('<YOUR CHOSEN GOOGLE FORM>')

	WebDriverWait(driver, 0.25).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='<DIV ID>']")))

	
	radio_button = driver.find_element(By.XPATH, "//div[@id='<DIV ID>']")
	radio_button.click()

	print("Click")


	submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
	submit_button.click()
	print("Submitted")

	driver.close()
	print("Success")
