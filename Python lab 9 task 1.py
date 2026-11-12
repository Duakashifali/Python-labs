# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:17:30 2026

@author: hp
"""

def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"

def run_vacuum(room_A, room_B):
    location = "A"

    print("\nInitial Conditions:")
    print("Room A:", room_A)
    print("Room B:", room_B)

    for i in range(4):

        if location == "A":
            status = room_A
        else:
            status = room_B

        action = vacuum_agent(location, status)

        print("Location:", location)
        print("Action:", action)

        if action == "Suck":
            if location == "A":
                room_A = "Clean"
            else:
                room_B = "Clean"

        elif action == "Move Right":
            location = "B"

        elif action == "Move Left":
            location = "A"

    print("Final Room A:", room_A)
    print("Final Room B:", room_B)

# Test Case 1
print("TEST CASE 1")
run_vacuum("Dirty", "Dirty")

# Test Case 2
print("\nTEST CASE 2")
run_vacuum("Clean", "Dirty")

# Test Case 3
print("\nTEST CASE 3")
run_vacuum("Dirty", "Clean")