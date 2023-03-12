import math

# Get user input for hours and minutes
hours = int(input("Enter hours (0-11): "))
minutes = int(input("Enter minutes (0-59): "))

# Convert hours to degrees and add the contribution of minutes
hour_degrees = (hours % 12) * 30 + (minutes / 60) * 30

# Convert minutes to degrees
minute_degrees = minutes * 6

# Calculate the absolute difference between the two angles
angle = abs(hour_degrees - minute_degrees)

# Calculate the lesser angle
if angle > 180:1
angle = 360 - angle

# Print the result
print("The lesser angle between the hour and minute hands is", angle,"degrees.")

