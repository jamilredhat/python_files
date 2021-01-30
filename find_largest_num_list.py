numbers = [22, 55, 66, 77, 22, 343, 784]
largest_num = 0
for a in numbers:
    if a > largest_num:
        largest_num = a
print(f'The largest number is: {largest_num}')