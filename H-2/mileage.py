# Leonardo Farinha H2
#Formula = Miles Driven / Gallons Used = MPG

miles_start = float(input("Please enter your current milleage (first fill up): "))
miles_end = float(input("Please enter the millage for your second fill up: "))
gals_used = float(input("Please enter number of gallons used: "))

mpg = ((miles_end - miles_start) / gals_used)

print("Your MPG is: ", mpg)
