#!/usr/bin/env python3
"""Tracking the positon of an alien that can move at different speeds."""

alien_0 = {'x_position': 0, 'y_postion': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a first alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x_position: " + str(alien_0['x_position']))

