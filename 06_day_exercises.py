#Exercises: Level 1

#1 Create an empty tuple

empty_tuple = ()

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ('Borja', 'Druso')
sisters = ('Tatiana', 'Muriel')

#3 Join brothers and sisters tuples and assign it to siblings

siblings = brothers + sisters

#4 How many siblings do you have?

print(len(siblings))

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = siblings + ('Toñi', 'Armando')
print(family_members)

#Exercises: Level 2

#1 Unpack siblings and parents from family_members

*siblings, mother, father = family_members
parents = (mother, father)
print(siblings)
print(parents)

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('Apple', 'Banana', 'Kiwi')
vegetables = ('Tomatoe', 'Onion', 'Eggplant')
animal_pr = ('Honey', 'Milk')

food_stuff_tp = fruits + vegetables + animal_pr

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

print(food_stuff_tp[len(food_stuff_tp) // 2], food_stuff_tp[len(food_stuff_tp) // 2 + 1])

#5 Slice out the first three items and the last three items from food_staff_lt list

print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

#6 Delete the food_staff_tp tuple completely

del food_stuff_tp

#7 Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)

print('Iceland' in nordic_countries)
