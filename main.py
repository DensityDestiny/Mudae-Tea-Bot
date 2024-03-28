import cv2
import mss
import pyautogui
import numpy as np
import easyocr
from PIL import Image
import time


with open('words.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip().split(',') for line in lines]


choice = input("Which game are you playing? ")
# Black Tea
if choice == "1":
    used_words = []
    time.sleep(1)
    reader = easyocr.Reader(['en'])
    monitor = {"left": 400, "top": 730, "width": 450, "height": 42}
    sct = mss.mss()
    while True:
        if pyautogui.position().y > 750 and pyautogui.position().x < 50:
            break 
        image = sct.grab(monitor)
        img_array = np.array(image)
        result = reader.readtext(img_array)
        final_result = ""
        for i in result:
            final_result += i[1]
        if "Destiny" in final_result and "Type" in final_result and "containing" in final_result:
            letters = final_result[-3] + final_result[-2] + final_result[-1]
            for i in range(len(lines)):
                if letters.lower() in lines[i][0].lower() and lines[i][0].lower() not in used_words:
                    pyautogui.write(lines[i][0].lower())
                    pyautogui.press("enter")
                    used_words.append(lines[i][0].lower())
                    time.sleep(0.5)
                    break
        elif "DISCORD NAME HERE" in final_result and "won" in final_result and "the" in final_result and "game" in final_result:
            pyautogui.write(":yay:")
            pyautogui.press("enter")
            time.sleep(1)
        elif "DISCORD NAME HERE" not in final_result and "won" in final_result and "the" in final_result and "game" in final_result:
            pyautogui.write(":frightened:")
            pyautogui.press("enter")
            time.sleep(1)
    

# Red Tea
if choice == "2":
    while True:
        letters = input("Enter the letters: ")
        if letters == 'n':
            break
        possible_words = []
        lenght = 3
        word = ''
        for num_words in range(25):
            for i in lines:
                if letters in i[0] and len(i[0]) == lenght:
                    word = i[0]
            if word != '':
                possible_words.append(word)
            word = '' 
            lenght += 1
        time.sleep(3)
        for i in possible_words:
            pyautogui.write(i)
            pyautogui.press('enter')
        pyautogui.write(':devious:')
        pyautogui.press('enter')
        print('The Job Is Done :devious:')
      
