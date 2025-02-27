# # Get the number of days attended from the user
# days_attended = int(input("Enter the number of days attended: "))

# # Check if the person has attended at least 15 days
# if days_attended >= 15:
#     print("You have completed 15 days of work.")
    
#     # Check if the person has attended more than 20 days
#     if days_attended > 20:
#         print("Congratulations! You are eligible for a casual leave.")
#     else:
#         print("You need to work more than 20 days to get a casual leave.")
# else:
#     print("You need to attend at least 15 days to qualify.")


# # Ask the user how many employees to check
# num_employees = int(input("Enter the number of employees: "))

# # Outer loop to check multiple employees
# for i in range(num_employees):
#     days_attended = int(input(f"\nEnter the number of days attended by Employee {i+1}: "))

#     # Check if the employee has attended at least 15 days
#     if days_attended >= 15:
#         print(f"Employee {i+1} has completed 15 days of work.")

#         # Direct condition instead of an unnecessary loop
#         if days_attended > 20:
#             print(f"Employee {i+1} is eligible for a casual leave.")
#         else:
#             print(f"Employee {i+1} needs to work more than 20 days to get a casual leave.")
    
#     else:
#         print(f"Employee {i+1} needs to attend at least 15 days to qualify.")


#WAP to convert temp from degree to fahernient 

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Taking user input for cities and distances
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")
dist1 = float(input(f"Enter the distance from {city1} to {city2} in km: "))

city3 = input("Enter the third city: ")
dist2 = float(input(f"Enter the distance from {city2} to {city3} in km: "))

cost_per_km = 5  
fare1 = dist1 * cost_per_km
fare2 = dist2 * cost_per_km
total_fare = fare1 + fare2
print(f"\nAirfare from {city1} to {city2}: Rs{fare1}")
print(f"Airfare from {city2} to {city3}: Rs{fare2}")
print(f"Total airfare for the journey ({city1} → {city2} → {city3}): Rs{total_fare}")


#wap to display the month of the year using user input 
# List of months
months = ["January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]
month_number = int(input("Enter a month number (1-12): "))
if 1 <= month_number <= 12:
    print(f"The month is {months[month_number - 1]}")
else:
    print("Invalid input! Please enter a number between 1 and 12.")

#wap to check if given number is odd or even 
num = int(input("enter the num :"))
if (num%2==0):
    print("the given number is even:",num)
else:
    print("the given number is odd:",num )
print(num)

#wap to calculate the interset rate that have deposited only in the leap year

year = int(input("Enter the deposit year: "))
if  (year % 400 == 0):
    print(f"{year} is a leap year. You can deposit money.")

    p = float(input("Enter the principal amount (Rs): "))
    r = float(input("Enter the annual interest rate (%): "))
    t = float(input("Enter the time in years: "))

    interest = (p * r * t) / 100
    print(f"Interest earned in {t} years: Rs{interest}")

else:
    print(f"{year} is not a leap year. Deposits are only allowed in leap years.")

