#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:19:05 2019

@author: jraising
"""

donors = {'William Gates, III': [653784.49, 1000.50], 
          'Mark Z': [16396.10, 30000, 20000.30],
          'Jeff B': [877.33],
          'Paul Allen': [708.42, 780, 444.20],
          'Satya':[ 1000, 500.33]
          }
         

def menu_selection(prompt, disp_dir):
    while True:
        response = input(prompt)
        if disp_dir[response]() == "Exit menu":
            break

def thankYou():
    fullName = input("please enter the full name: ")
    if fullName == "list":
        for k,v in donors.items():
            print(k)
    if fullName not in donors.keys():
        donors[fullName] = []
        
 # Use try/except in your code   
    amount = 0
    while amount <= 0: 
        try:
            amount = int(input("How much would you like to donate?  "))
        except ValueError:
            print("Enter a number")
        else:
            if amount > 0:
                print(amount)
                donors[fullName].append(amount)
            else:
                print("Enter a valid amount")
        
    
        
   
        
    
    print(f'{fullName}, Thank you very much for your donation of ${amount}')

def report():   
    print(f'{"Donor Name": <35}{"Total Given":30}{"Num Gifts":22}{"Average Gift":25}')
    print('-'*102)
    
    [print(f'{k:20} {sum(v):{25}.2f} {len(v):25} {(sum(v)/len(v)):{25}.2f}') for k,v in donors.items()]
        
def letter():
    for k,v in donors.items():
#         print(f'{k}, Thank you very much for your donation of ${sum(v):.2f}')
         with open(f'{k}.txt', 'w') as file:
             file.write(f'Subject: Thank You \n Dear {k}, \n Thank you very much for your donation of ${sum(v):.2f} ')
             
        
    

def quit():
    print("You are quitting the menu")
    return "Exit menu"

#def thankYou_menu():
#    menu_selection(thankYou_prompt,thankYou_dispatch)
    
       
main_prompt = (" Select 1 to donate, 2 to Create a Report, 3 to Send a Thank You, or q to quit >> ")

main_dispatch = {"1" : thankYou,
                 "2" : report,
                 "3" : letter,
                 "q" : quit
                }

#thankYou_prompt = ("Enter full name >> ")
#
#thankYou_dispatch = {"list": print(donors.keys()),
#                     
#                     "q": quit
#                     }

menu_selection(main_prompt,main_dispatch)