from selenium import webdriver
import time

#c stores the location of chrome driver you need to install it. The r represents a raw file
c = r"C:\Users\Harshit\Downloads\chromedriver_win32 (1)\chromedriver.exe"

#opening whatsapp using chrome driver
driver = webdriver.Chrome(c)
driver.get("http://web.whatsapp.com/")

c  = input("Press any key after scanning the QR code")
mes = r"Hello"
while True:

	try:
		#this class is there for unread messages
		m = driver.find_element_by_class_name("ZKn2B")
		m.click()	
	
		msg = driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")
		msg.send_keys(mes) # send the message

		button = driver.find_element_by_class_name('_1U1xa')
		button.click()

	except:
		continue 

	