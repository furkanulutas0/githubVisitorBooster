import selenium
from selenium import webdriver
import time
from datetime import datetime
import random

now = datetime.now()  
current_time = str(datetime.ctime(now))

driver = webdriver.Chrome() # You must select a webdriver. If you don't want to use Chrome, you can use Mozilla.
url = "https://www.github.com/furkanulutas0" # This program was developed for Github. If you want to use another website's url, you have to change some codes in the program.

print(f"Calling URL >> {url}")
try: 
    file = open("log.txt", "a") # This is your log file.
    file.write(f"{current_time} Module Started\n")
    file.close()
    ping_amount = int(input("How many times do you want to call the url: ")) 
    driver.get(url)
    print(f"Url called first time. >> {url}")
except:
    print("Calling failed 404")

counter = 1



def write():
    now = datetime.now()
    current_time = str(datetime.ctime(now))
    file = open("log.txt", "a")
    file.write(f"{current_time} - Url called successfully {counter} time.\n")
    file.close()

def error():
    now = datetime.now()
    current_time = str(datetime.ctime(now)) 
    file = open("log.txt", "a")
    file.write(f"{current_time} - Url haven't called. \n")
    file.close()

while True:
    try:
        if counter == ping_amount:
            driver.close()
            break
        else:
            second = random.choice(range(5,60))
            time.sleep(second)
            counter = counter + 1
            print(f"Url called {counter} time. (waited : {second*1000}ms )")
            write()
            driver.refresh()
    except:
        print("The program encountered an error, STOPING")
        error()
        break



