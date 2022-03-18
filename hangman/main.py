#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 19:12:14 2022

@author: karan
"""
import random
from hangman_life import lives
from hangman_guessing import guess_list
from hangman_life import game_name

def getString(result):
    string=str()
    for i in range(len(result)):
        string+=result[i]
    return string

guess=list(random.choice(guess_list).lower())
length=len(guess)
#print the game name

print(game_name)

#create a result 
result=[]
string=str()
for i in range(length):
    result.append("_")

#take input from user for tries==len(guess)

tries=len(guess)
while tries!=0:
    try:
        user_letter=input("Enter a letter")
        if len(user_letter)!=1 or not user_letter.isalpha():
            raise Exception
        #check if the letter is correct
        for i in range(length):
            if user_letter==guess[i]:
                result[i]=user_letter        
        print(getString(result))
        if user_letter not in guess:
            print(lives[tries])
            tries-=1
        if tries==0:
            print(lives[0]+"\nYou lose!")
        elif result==guess:
            print("You win!")
            break
    except Exception:
        print("Error: Enter a single letter")