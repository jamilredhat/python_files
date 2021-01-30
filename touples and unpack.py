list1 = [ 1, 2, 3, 4]
list2 = ['a', 'b']
dictionary1 = {
    'a': 'book',
    'b': 'car'
}

touples1 = (1, 2, 3, 4)            # touple value can not be changed.
print(touples1[0])
list2[1] = 'g'                  # list  value can be changed
print(list2[1])

#touples1[0] = 5                 # produce error

a, b, c, d = touples1           # assignes touples1[0] to a and touples1[1] to b ....
for i in a, b, c, d:
    print(i)