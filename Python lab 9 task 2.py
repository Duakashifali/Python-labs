# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:21:35 2026

@author: hp
"""

# Object Oriented Vacuum Environment

class VacuumEnvironment:

    def __init__(self):
        self.rooms = {
            "A": "Dirty",
            "B": "Dirty"
        }

    def clean_room(self, location):
        self.rooms[location] = "Clean"

    # Count dirty rooms
    def count_dirty_rooms(self):
        count = 0

        for room in self.rooms:
            if self.rooms[room] == "Dirty":
                count += 1

        return count

class VacuumAgent:

    def __init__(self, environment):
        self.environment = environment
        self.location = "A"

    def act(self):

        if self.environment.rooms[self.location] == "Dirty":
            print("Action: Suck")
            self.environment.clean_room(self.location)

        elif self.location == "A":
            print("Action: Move Right")
            self.location = "B"

        else:
            print("Action: Move Left")
            self.location = "A"

# Create environment and agent

environment = VacuumEnvironment()
agent = VacuumAgent(environment)

# Run agent

for i in range(4):

    print("\nCurrent Location:", agent.location)

    agent.act()

    dirty = environment.count_dirty_rooms()

    print("Dirty Rooms Remaining:", dirty)

print("\nFinal Room Status:")
print(environment.rooms)