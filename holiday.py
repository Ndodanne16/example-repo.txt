import math

#programme that calculates user holiday costs (planes, hotel, car rental)

#ask user for destination, duration of stay, car rental duration
city_flight = input("Please choose a city you will be flying to between Lisbon and Amsterdam:").lower()

num_nights = int(input("Please enter the number of nights you will be staying at the hotel:" ))

rental_days = int(input("Please enter the number of days you would like to rent a vehicle:"))

#formula for flight costs to respective cities
def plane_cost(city_flight):
       if city_flight == "lisbon":
           return(12000)
       elif city_flight == "amsterdam":
            return (10000)
       else:
            return (0)

if city_flight == "lisbon":
     print("The cost for your flights to Lisbon will be R12000")
elif city_flight == "amsterdam":
     print("The cost for your flights to Amsterdam will be R10000")
else: print("Error.")

#formula for hotel cost
def hotel_cost (num_nights):
    return num_nights * 1200 
print(f"The cost of your hotel stay will be R{hotel_cost(num_nights)}")
    
#formula for car rental
def car_rental(rental_days):
    return rental_days * 990
print(f"The cost of your car rental will be R{car_rental(rental_days)}")

#calculating total holiday cost
def holiday_cost(city_flight, num_nights, rental_days): 
    holiday_total = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)
    return holiday_total


print ("The total cost of your holiday will be R" + str(holiday_cost(city_flight, num_nights, rental_days)))
















