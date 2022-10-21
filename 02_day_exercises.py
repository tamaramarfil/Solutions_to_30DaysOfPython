#Write a python comment saying 'Day 2: 30 Days of python programming'
#Day 2: 30 Days of python programming

#Declare a first name variable and assign a value to it
first_name = 'Tamara'

#Declare a last name variable and assign a value to it
last_name = 'Marfil'

#Declare a full name variable and assign a value to it
space=(' ')
full_name = first_name + space + last_name

#Declare a country variable and assign a value to it
country = 'España'

#Declare a city variable and assign a value to it
city = 'Málaga'

#Declare an age variable and assign a value to it
age = 41

#Declare a year variable and assign a value to it
year = 2022

#Declare a variable is_married and assign a value to it
is_married = False

#Declare a variable is_true and assign a value to it
is_true = True

#Declare a variable is_light_on and assign a value to it
is_light_on = False

#Declare multiple variable on one line
skills = ['Java', 'Python', 'SQL']

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(skills))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Compare the length of your first name and your last name
print(len(first_name) == len(last_name))

#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)

#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)

#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

#The radius of a circle is 30 meters.
#Take radius as user input and calculate the area
radius=(input('¿cuál es el radio de la circunferencia?'))
radius=int(radius)

#Calculate the area of a circle and assign the value to a variable name of area_of_circle
pi = 3.14
area_of_circle = pi * (radius * radius)
print(area_of_circle)

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * radius
print(circum_of_circle)

'''
Use the built-in input function to get first name, last name,
country and age from a user and store the value to their corresponding variable names
'''
first_name = (input('Cuál es tu nombre'))
last_name = (input('cuál es tu apellido'))
country = (input('cual es tu país'))
age = (input('cuál es tu edad'))
print(first_name)
print(last_name)
print(country)
print(age)

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
