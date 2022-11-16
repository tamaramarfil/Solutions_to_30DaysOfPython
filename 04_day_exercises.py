#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

print(' '.join(['Thirty', 'Days', 'Of', 'Python']))

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

print(' '.join(['Coding', 'For', 'All']))

#3 Declare a variable named company and assign it to an initial value "Coding For All".

company = 'Coding For All'

#4 Print the variable company using print().

print(company)

#5 Print the length of the company string using len() method and print().

print(len(company))

#6 Change all the characters to uppercase letters using upper() method.

print(company.upper())

#7 Change all the characters to lowercase letters using lower() method.

print(company.lower())

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string.

print(company[7:])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.

print('Coding For All'.index('Coding'))

#11 Replace the word coding in the string 'Coding For All' to Python.

print('Coding For All'.replace('Coding', 'Python'))

#12 Change Python for Everyone to Python for All using the replace method or other methods.

print('Python for Everyone'.replace('Everyone', 'All'))

#13 Split the string 'Coding For All' using space as the separator (split()) .

print('Coding For All'.split(' '))

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

companies = ("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon")
print(companies.split(','))

#15 What is the character at index 0 in the string Coding For All.

print(company[0])

#16 What is the last index of the string Coding For All.

print(company[-1])

#17 What character is at index 10 in "Coding For All" string.

print(company[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.

frase = 'Python For Everyone'
print(frase[0] + frase[7] + frase[11])

#19 Create an acronym or an abbreviation for the name 'Coding For All'.

frase = 'Coding For All'
print(frase[0] + frase[7] + frase[11])

#20 Use index to determine the position of the first occurrence of C in Coding For All.

print('Coding For All'.index('C'))

#21 Use index to determine the position of the first occurrence of F in Coding For All.

print('Coding For All'.index('F'))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.

print('Coding For All People'.rfind('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print('You cannot end a sentence with because because because is a conjunction'.index('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print('You cannot end a sentence with because because because is a conjunction'.replace('because', ''))

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print('You cannot end a sentence with because because because is a conjunction'.find('because'))

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print('You cannot end a sentence with because because because is a conjunction'.replace('because', ''))

#28 Does ''Coding For All' start with a substring Coding?

print('Coding For All'.startswith('Coding'))

#29 Does 'Coding For All' end with a substring coding?

print('Coding For All'.endswith('Coding'))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.

print('   Coding For All      '.strip())

#31 Which one of the following variables return True when we use the method isidentifier():

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

print('-'.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

#33 Use the new line escape sequence to separate the following sentences.

print('I am enjoying this challenge.\nI just wonder what is next.')

#34 Use a tab escape sequence to write the following lines.

print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

#35 Use the string formatting method to display the following:

print('radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.')

#36 Make the following using string formatting methods:

print('8 + 6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')