# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:12:02 2021

@author: ergun
"""

def getName():
    #TODO: Add your full name instead of Lionel Messi
    return "Koorosh Shakoori"

def getStudentID():
    #TODO: Replace X's with your student ID. It should stay as a string and should have exactly 9 digits in it.
    return "X00000000"


def find_winner(bid_list):
     #TODO: Implement your logic here
    #To prevent mutiple entries by a single customer, we will only accept their first entry.
    #To do so, we will use dictionaries as it will only accept unique keys, however, we need to use the reversed list to keep the very first entry.
    #Afterwards, we will return the values to its original list format.
    
    bid_list.reverse()
    bid_dict = dict(bid_list)
    bid_list = [(customer, bid_dict[customer]) for customer in bid_dict]
    
    #In this step, we will remove the negative bids using list comprehension,
    #While simultaneously sorting the list in ascending order using the native sorted() function and a lambda function as key.
    
    bid_list = sorted([x for x in bid_list if x[1] >= 0], key=lambda x: x[1])
    
    #Now, with the sorted list, we will check for duplicates in minimum values, if there are any.
    #In case of duplicates, we remove them by making a new list without them.
    #This process goes on until we encounter either a unique value hence the winner or an empty list in which case there are no winners for the competition.
    
    while True:
        
        #This block checks if the list is empty and if so assigning No Winner for the contest.
        if len(bid_list) == 0:
            winner = ("No Winner", -1)
            break
        
        #This block checks for duplicates at the beginning of the list and makes a new list without those entries.
        elif bid_list[0][1] == bid_list[1][1]:
            duplicate = bid_list[0][1]
            bid_list = [x for x in bid_list if x[1] > duplicate]
            
        #In case none of the statements above are satisfied it means the first element in the list which is the least is unique, hence the winner.
        else:
            winner = bid_list[0]
            break
            
    return winner


