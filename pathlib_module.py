from pathlib import Path

a = Path("testrrr")     # pass the directory name to work on

print(a.exists())
#a.mkdir()          # The directory which was given as an argument will be created.

# search files in a directory

b = Path('system_scripts')
#print(a.glob('*'))      # This returns generator object. And for loop can be used to generate result.

for file_name in b.glob('*'):
    print(file_name)


