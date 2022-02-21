import pyautogui
import time
#if u have low spec pc please use less number of messages
print("Welcome to Rick Spam ")
a= input("Enter the message: ")
b= int(input("How many times ? : "))
t = 10
while t!= 0:
  print(t)
  time.sleep(1)
  t =t - 1
print("LET THE SPAM START !!!!!!")
for i in range(0,b):
        pyautogui.typewrite(a + '\n')