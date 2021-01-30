import sys

print(f'Total number of arguments are {len(sys.argv)}')
for a in range(len(sys.argv)):
    print(sys.argv[0])                          #sys.argv[0] is the script file name.
    print(sys.argv[a])                          # Prints script file name and all arguments.
