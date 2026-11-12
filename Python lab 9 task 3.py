# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:24:38 2026

@author: hp
"""

# Improved Vacuum Cleaner Agent
class VacuumEnvironment:

    def __init__(self):
        self.rooms = {
            "A": "Dirty",
            "B": "Dirty"
        }

    def clean_room(self, location):
        self.rooms[location] = "Clean"

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

        # Check whether both rooms are clean
        if self.environment.count_dirty_rooms() == 0:
            return "Stop"

        # Check current room
        if self.environment.rooms[self.location] == "Dirty":
            self.environment.clean_room(self.location)
            return "Suck"

        elif self.location == "A":
            self.location = "B"
            return "Move Right"

        else:
            self.location = "A"
            return "Move Left"

# Create environment and agent

environment = VacuumEnvironment()
agent = VacuumAgent(environment)

# Execute agent
while True:

    print("\nCurrent Location:", agent.location)

    action = agent.act()

    print("Action:", action)

    if action == "Stop":
        print("Both rooms are clean. Agent stopped.")
        break

    print("Dirty Rooms Remaining:",
          environment.count_dirty_rooms())

print("\nFinal Room Status:")
print(environment.rooms)