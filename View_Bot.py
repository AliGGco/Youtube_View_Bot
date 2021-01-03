from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver1 = webdriver.Chrome(executable_path='chromedriver')
driver2 = webdriver.Chrome(executable_path='chromedriver')
driver3 = webdriver.Chrome(executable_path='chromedriver')
driver4 = webdriver.Chrome(executable_path='chromedriver')
#you can add your links to these drivers
driver1.get("Video_Links")
driver2.get("Video_Links")
driver3.get("Video_Links")
driver4.get("Video_Links")

while True:
    sleep(300) #here you can set the time for reloading the page
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
    driver4.refresh()
