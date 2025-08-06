#Selenium testing

'''
use webdriver to test a web application
use by to locate elements
use keys to interact with elements
use edge
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome import Service

# Set up the Chrome WebDriver service
service = Service(executable_path='/chrome-win64')  # Update with your Edge WebDriver path
service.navigate_to('')
service.start()
service.close()
# Initialize the WebDriver
driver = webdriver
driver.Chrome.find_element(webdriver)

# By class usage
className = By.CLASS_NAME


#Using Keys
scrollDown = Keys.ARROW_DOWN

#