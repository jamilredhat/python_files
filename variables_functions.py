name = "Jamil Ahmed"
age = 233

print(len(name))
print(len(str(age)))
print(name.upper())
print(name.lower())
print(name.isupper())   # check if upper
print(name.islower())   # check if string is a lower case
print(name.isnumeric())  # check if variable value is numeric.
print(name.find('i'))   # returns the index number of the letter. Returns -1 if not found.
print(name.replace('Ahmed', 'Ahmad')) # will replace Ahmed with Ahmad
print(name.replace('e', 'a')) # replace all ees into aas
#name = "Jameel Ahmed"
#print(name.replace('e', 'a'))   # Replace all ees into aas

# check if a string is pereset in a variable
print('jamil' in name)  # Returns True/False
# 'Jamil' in name
if 'Jamil' in name:
    print("Found Jamil in variable.")
else:
    print("Jamil not found")
