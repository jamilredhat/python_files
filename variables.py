name = "Jamil Ahmed"
age = 26
is_new = True

print("Name: " + name)

print(f'{name} is {age} old and is a new patient {is_new}')



#Check the type of a variable.
print(type(age))
print(type(name))

print(f'printing * times age')
print('*' * age)

#Print '
print("test's string")

#Print "
print('"Test" abc')

#Print character by their index. -1 is the last character
a = "Who are you"
print(f'{a[0]} {a[2]} {a[5]} {a[8]} {a[-2]} ')
print(a[0:3])
print(a[:5])
print(a[-2:])   # Start printing from the second last position. -1 is the last one0
print(a[:])     # prints all
#Print multi line string

print(''' 
This is 
multi line "" works here '' also works here
string    
''')