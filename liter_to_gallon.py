#This code converts l/100km to mpg and vice versa
# Conversion constants
MILES_PER_KILOMETER = 0.621371
LITERS_PER_GALLON = 3.785411784

def liters_100km_to_miles_gallon(liters_per_100km):
    # Convert fuel consumption from l/100km to mpg
    miles_per_gallon = 100 / (liters_per_100km / LITERS_PER_GALLON) * MILES_PER_KILOMETER
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles_per_gallon):
    # Convert fuel consumption from mpg to l/100km
    liters_per_100km = 100 / (miles_per_gallon / MILES_PER_KILOMETER) * LITERS_PER_GALLON
    return liters_per_100km

# Test the functions
liters_per_100km = 7.0
miles_per_gallon = 33.6

converted_to_mpg = liters_100km_to_miles_gallon(liters_per_100km)
converted_to_l_100km = miles_gallon_to_liters_100km(miles_per_gallon)

print(f"{liters_per_100km} l/100km is approximately {converted_to_mpg:.2f} mpg.")
print(f"{miles_per_gallon} mpg is approximately {converted_to_l_100km:.2f} l/100km.")
