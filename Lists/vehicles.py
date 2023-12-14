#!/usr/bin/env python3

"""
- Making a list of fleet of cars.
- Iterate over the list using for loop.
- print 3 statements to show the use of indentation 
  after the for lop statement
  N/B: Rem to overcome the logic error which python may not capture
"""
vehicles = ["porsche", "bmw x1 m", "mercedes benz"]
for vehicle in vehicles:
    print("One among the car fleets I own is " + vehicle.title() + "!")
    print("Amongst the three, " + vehicles[0].title()+ " is my favorite!" + "\n")
print("All in all,I thank God for such blesings.")
