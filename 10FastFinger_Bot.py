from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()

option = input("[1] typing-test\n[2] Multiplayer\n\nYour option: ")
delay = float(input("The delay between each word (0 is also fine ;): "))

if option == "1":
    browser.get("https://10fastfingers.com/typing-test/english")
    sleep(0.2)
    field = browser.find_element_by_id("inputfield")
elif option == "2":
    browser.get("https://10ff.net/multiplayer")
    input("Enter username in the browser and press ENTER in the browser and then here in the console...")
    sleep(0.2)
    field = browser.find_element_by_tag_name("input")
else:
    print("Can you not read idiot?! Only '1' & '2' are valid options!")
    sleep(2)
    exit()

input("Press ENTER to start!!!")
while True:
    word = browser.find_element_by_class_name("highlight")
    field.send_keys(word.text+" ")
    sleep(delay)