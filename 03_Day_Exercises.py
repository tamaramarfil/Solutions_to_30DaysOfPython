#1
my_age = 41

#2
my_height = 1.60

#3 
var_complex = 2 + 2j

#4
base = int(input('Indique la base del triángulo'))
height = int(input('Indique la altura del triángulo'))
area = 0.5 * base * height
print('The area of the triangle is:', area)

#5 
side_a = int(input('Indique lado a'))
side_b = int(input('Indique lado b'))
side_c = int(input('Indique lado c'))
perimeter = side_a+side_b+side_c
print('The perimeter of the triangle is:', perimeter)

#6
length = int(input('Introduzca el largo del rectánculo'))
width = int(input('Introduzca el ancho del rectángulo'))
area_rectangle = length * width
print('El área del rectánculo es', area_rectangle)
perimeter_rectangle = 2 * (length * width)
print('El perímetro del rectángulo es', perimeter_rectangle)

#7
r_circle = int(input('Indique el radio del círculo'))
pi = 3.14
area_circle = pi * r_circle * r_circle
circumference_circle = 2 * pi * r_circle
print('El área del círculo es:', area_circle)
print('La circunferencia del círculo es:', circumference_circle)

#8 Calculate the slope, x-intercept and y-intercept of y = 2x -2

def funcion_afin_x(x):
    y = (2 * x) - 2
    return y

def funcion_afin_y(y):
    x = (y + 2) / 2
    return x

x_intercept = 0
y_x_intercept = funcion_afin_x(0)
print('X Intercept:', x_intercept, y_x_intercept)

y_intercept = 0
x_y_intercept = funcion_afin_y(0)
print('Y Intercept:', x_y_intercept, y_intercept, )

slope1 = (y_intercept-y_x_intercept)/(x_y_intercept-x_intercept)
print('Slope:', slope1)

#9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

import numpy as np
x1, x2, y1, y2 = 2, 6, 2, 10
slope2 = (y2-y1)/(x2-x1)
print('Slope:', slope2)
euc_dist = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print('Distance Euclidean:', euc_dist)

#10 Compare the slopes in tasks 8 and 9.

if slope1 == slope2:
    print('Slopes are correct')

#11
for x in range(-5,5):
    if((x ** 2 + 6 * x + 9)) == 0:
        print('Para el valor de x =', x ,'y es igual a cero')

#12
print(len('python'))
print(len('dragon'))
print(len('python') != len('dragon'))

#13
print('on' in 'Python') and ('on' in 'Dragon')

#14
print('jargon' in 'I hope this course is not full of jargon')

#15
print('on' not in 'python' and 'on' in 'dragon')

#16
len_python = (len('python'))
print(type(len_python))
len_python = float(len_python)
print(type(len_python))
len_python = str(len_python)
print(type(len_python))

#17
num_par = int(input('Introduzca un número'))
if num_par % 2 == 0:
    print('El número es par')
else:
    print('El número es impar')

#18
value_1 = 7//3
value_2 = int(2.7)
if value_1 == value_1:
    print('Value1 is equal to value2')
else:
    print('Value1 is not equal to value2')
    
#19
if type('10') == type(10):
    print('Are equal')
else:
    print('Are not equal')

#20
if int(9.8) == 10:
    print(True)
else:
    print(False)

#21 
hours = int(input('Indique las horas'))
rate_per_hour = int(input('Indique el pago por hora'))
print('Tu sueldo semanal es de', hours*rate_per_hour)

#22
years = int(input('Indique los años'))
seconds_to_live = years * 365 * 24 * 60 * 60
print('Has vivido', seconds_to_live, 'segundos')

#23 Write a Python script that displays the following table
for n in range(1, 6):
    print(n, n**0, n**1, n**2, n**3)
