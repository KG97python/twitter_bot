from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com')
        time.sleep(1)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

# modify the range to the number of likes you would like to do

    def like_tweet(self, entry3, entry4):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + str(entry3) + '&src=typed_query')
        pyautogui.moveTo(2000, None, 1)
        time.sleep(2)
        n = int(str(entry4))
        for i in range(n+1):
            pyautogui.click(pyautogui.locateCenterOnScreen('new.png'), duration=1)
            time.sleep(0.5)
            pyautogui.moveTo(2000, None, 1)
            time.sleep(0.5)
            pyautogui.click(pyautogui.locateCenterOnScreen('new.png'), duration=1)
            time.sleep(0.5)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(0.5)
            pyautogui.moveTo(2000, None, 1)
            time.sleep(0.5)
            if None:
                print('image not found!!!!!!')

    # modify range to the amount of people you would like to auto follow

    def follow(self, entry3, entry5):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + str(entry3) + '&f=user')
        n = int(str(entry5))
        pyautogui.moveTo(2000, None, 1)
        time.sleep(2)
        for i in range(n+1):
            for j in range(1, 9):
                pyautogui.click(pyautogui.locateCenterOnScreen('follow.png'), duration=1)
                time.sleep(0.2)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(0.2)
            pyautogui.moveTo(2000, None, 1)
            time.sleep(0.2)

def execute():
    log = TwitterBot(str(entry1.get()), str(entry2.get()))
    log.login()
    log.like_tweet(entry3.get(), entry4.get())
    log.follow(entry3.get(), entry5.get())

# ditinker gui
window = Tk()
window.geometry("2000x1080")
emails = Label(window, text="enter your email here", font='times 24 bold')
emails.grid(row=0, column=0)
entry1 = Entry(window)
entry1.grid(row=0, column=6)

password = Label(window, text="enter your password here", font='times 24 bold')
password.grid(row=2, column=0)
entry2 = Entry(window)
entry2.grid(row=2, column=6)

hashtag = Label(window, text="enter your hashtag here", font='times 24 bold')
hashtag.grid(row=3, column=0)
entry3 = Entry(window)
entry3.grid(row=3, column=6)

like = Label(window, text="how many likes do you want to automate?", font='times 24 bold')
like.grid(row=6, column=0)
entry4 = Entry(window)
entry4.grid(row=6, column=6)

follow = Label(window, text="how many follow request do you want to automate?", font='times 24 bold')
follow.grid(row=8, column=0)
entry5 = Entry(window)
entry5.grid(row=8, column=6)

exitbutton = Button(window, text="Exit", command=window.destroy, width=12, bg='gray')
exitbutton.grid(row=30, column=5)

b1 = Button(window, text=" GO ", command=execute, width=12, bg='gray')
b1.grid(row=10, column=5)
window.mainloop()