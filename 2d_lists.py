number = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
print(f'third "2" item of the second "2" item is:  {number[1][2]}')
# Change value
number[1][2] = 55		   # Assign/change value to third (6) item of second row ([4, 5, 6])
number.append([10, 11, 12])         #Add an item at the end of the list
number.insert(2, [10, 11, 12] )     # insert an item at the position 2.
#number.remove([10, 11, 12])         # Remove an ite.
#number.clear()                      # Remove all items
# number.pop()                      Removes last item or ite from
for main in number:
    for a in main:
        print(a)

print(15 in number)             # finds a item in list and return True or False. 15 is not in number list therefore False.
print(15 in number[2])          # 15 is present in third item number[2] of the list therefore True.
print(number.count([10, 11, 12]))   # how many times a number is present in a list. 2

numbers = [ 3, 5, 9, 1, 4, 5, 1, 7]
print(numbers.count(1))
numbers.sort()                  # First sort and then print
print(numbers)
numbers.reverse()               # reverse sort. Must .sort first before running .reverse.
print(numbers)

# remove duplicate numbers.
numbers = [ 3, 5, 9, 1, 4, 5, 1, 7]
dup_num = []
for a in numbers:
    if a not in dup_num:
        dup_num.append(a)
print(dup_num)
