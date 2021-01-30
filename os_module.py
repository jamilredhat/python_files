import os

def interactive_input(dir):
    comnd = "ls "+(dir)                     # to provide multiple arguments to os.system, first make a command and add multiple items in it then provide that command as an argumnet to os.system.
    os.system(comnd)                        # directly prints results to terminal. print statement is not required and also can not return anything using return command.

                                            #os.system can only be used to print results on screen. can not be saved in variable and can not be used.


def return_command_results():
    dir_list = os.popen("ls").readlines()
    return dir_list


for dir in return_command_results():
    print(dir)

print(len(return_command_results()))

print(os.popen('ls').read())                # Returns raw value
print(os.popen('ls').readline())            # Returns first line.
print(os.popen('ls'))


