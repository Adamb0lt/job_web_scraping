from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# function for loggin in to linkedin that will be imported into spider
def login_linkedin():
    # launches the browser. i need to enter my chrome dev path
    driver = webdriver.Chrome(executable_path='')
    driver.get('https://www.linkedin.com/login')


    # for finding html element with username and password
    # common practice for html element to have id as password and username
    # Key
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password + Keys.RETURN)

    time.sleep(5) # waits for login to complete for 5 seconds


    cookies = driver.get_cookies()
    driver.quit()
    return cookies
