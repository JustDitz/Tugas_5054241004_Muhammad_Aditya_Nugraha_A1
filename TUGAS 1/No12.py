# No 12
    
# Input
Speed = float(input("Jet's takeoff speed: ")) * (1000 / 3600) 
Distance = float(input("Distance of an aircraft-carrier: "))

# Main
Acceleration = (pow(Speed, 2) / (2*Distance))
Time = Speed / Acceleration
# Output
print(f"Acceleration: {Acceleration:.2f} m/s^2")
print(f"Time: {Time:.2f} seconds")