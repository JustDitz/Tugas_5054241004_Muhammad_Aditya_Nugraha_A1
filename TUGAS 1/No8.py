import math

# No 8

Population = int(input("Enter the Community's Population: "))
print(f"Magnitude: {((math.ceil(Population/3))*2*14)}L/Day\nCost of Water Saved: {((math.ceil(Population/3))*150)}$")