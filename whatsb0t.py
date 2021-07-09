from selenium import webdriver
import os
os.system('cls' if os.name=='nt' else 'clear')
print("""
         _         _   ___ _     __  _   
 __ __ _| |_  __ _| |_/ __| |__ /  \| |_ 
 \ V  V / ' \/ _` |  _\__ \ '_ \ () |  _|
  \_/\_/|_||_\__,_|\__|___/_.__/\__/ \__|
 ===================================================>>>                                        
 ||* This software is used to automatically send messages in whatsapp.
 ||* Designed for joke purposes.
 ||* Illegal use belongs to the user.
 ||* SammySec whatSb0t version: 1.0 new version AhmmySec
 ===================================================>>>
 """)

def firef():
    try:
        driver = webdriver.Firefox()
        driver.get('https://web.whatsapp.com/')
    except:
        print("Please install Selenium Firefox Driver.")
    #Start sending message
    name = input('Enter the name of user or group : ')
    msg = input('Enter your message : ')
    count = int(input('Enter the count : '))
    input('Enter anything after scanning QR code')
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()
    print(" ===================================================>>>")
    for i in range(count):
        msg_box = driver.find_element_by_class_name('_3u328')
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
        say = i
        say = say + 1
        print("["+str(say)+"]"+" => Sending")
    print(" ===================================================>>>")
    print("FINISH")
    #finish sending message

def chrom1():
    try:
        driver = webdriver.Chrome()
        driver.get('https://web.whatsapp.com/')
    except:
        print("Please install Selenium Chrome Driver.")
    #Start sending message
    name_1 = input('Enter the name of user or group : ')
    msg = input('Enter your message : ')
    count = int(input('Enter the count : '))
    input('Enter anything after scanning QR code')
    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name_1))
    user.click()
    print(" ===================================================>>>")
    for i in range(count):
        msg_box = driver.find_element_by_class_name('_3u328')
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
        say = i
        say = say + 1
        print("["+str(say)+"]"+" => Sending")
    print(" ===================================================>>>")
    print("FINISH")
    #finish sending message
def starting():
    print("""    1. Firefox    2. Chrome    """)
    slct1 = input("Select your web browser!  ")

    if slct1 == "1":
        firef()
    elif slct1 == "2":
        chrom1()
    else:
        print("Please, select 1 or 2 ")
        starting()
starting()