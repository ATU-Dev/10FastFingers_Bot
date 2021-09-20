# YOU NEED TO INSTALL AND SET UP "SELENIUM"
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("https://10fastfingers.com/typing-test/english")

print(driver.title)
delay = float(input("The delay between each word: "))
field = driver.find_element_by_id("inputfield")
for i in range(400):
    word = driver.find_element_by_class_name("highlight")
    field.send_keys(word.text)
    field.send_keys(" ")
    sleep(delay)

sleep(3)
driver.quit()