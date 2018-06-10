#Leonardo Farinha

#https://runestone.academy/runestone/static/thinkcspy/SimplePythonData/Exercises.html
#excercise 7

p = float(input("Enter the amount of the principal: "))
t = int(input("Enter the number of years: "))
r = float(input("Enter the nominal interest: "))
n = 12

a = (1 + (r / n))

result = 1
for x in range(t*n):
    result *= a

result = p * result

print("Result: ", result)
