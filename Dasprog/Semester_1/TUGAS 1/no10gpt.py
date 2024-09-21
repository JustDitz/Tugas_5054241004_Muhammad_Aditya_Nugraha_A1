def calculate_water_savings_and_cost(population):
    # Constants
    people_per_toilet = 3  # Number of people per new toilet
    flushes_per_day = 14  # Number of flushes per toilet per day
    old_toilet_water_per_flush = 15  # Liters of water used by old toilet per flush
    new_toilet_water_per_flush = 2  # Liters of water used by new toilet per flush
    toilet_cost = 150  # Cost of each new toilet in dollars

    # Calculate the number of new toilets needed
    num_new_toilets = population // people_per_toilet

    # Calculate daily water usage with old and new toilets
    old_water_usage_per_day = population * flushes_per_day * old_toilet_water_per_flush / people_per_toilet
    new_water_usage_per_day = num_new_toilets * flushes_per_day * new_toilet_water_per_flush

    # Calculate water saved per day in liters
    water_saved_per_day = old_water_usage_per_day - new_water_usage_per_day

    # Calculate the total cost of new toilets
    total_cost = num_new_toilets * toilet_cost

    return water_saved_per_day, total_cost

# Input: Population
population = int(input("Enter the community population: "))

# Calculate water savings and cost
water_saved, cost = calculate_water_savings_and_cost(population)

# Output
print(f"Water saved per day: {water_saved:.2f} liters")
print(f"Total cost for new toilets: ${cost:.2f}")
