import subprocess


# subprocess.Popen(['ls', '-lt', '/home'])        # print output on screen. Output can not be saved in variable.

# Following will run command and redirect output and errors to subprocess.PIPE which can then be accessed using variable.communicate() method

test = subprocess.Popen(['ls', '-lt', '/home'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
output, errors = test.communicate()               # Access output
for line in output.splitlines():
    print(line)
print('---------------------------------------------')
print(output)
print(errors)

#---------------------------------------------------------------------------------------------------#
# To save output to a file.
error_file = "/home/jamil/err_file"
out_file = "/home/jamil/out_file"
output_to_file = open(out_file, 'w+')
error_to_file = open(error_file, 'w+')
kernel_version = subprocess.Popen(['uname', '-r'], stderr=error_to_file, stdout=output_to_file, universal_newlines=True)

testout, testerr = kernel_version.communicate()

#---------------------------------------------------------------------------------------------------#

# | functionality

first_cmd = subprocess.Popen(['ls', '/bin'], stdout=subprocess.PIPE, universal_newlines=True)
second_cmd = subprocess.Popen(['wc', '-l'], stdin=first_cmd.stdout, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
first_cmd.stdout.close()
#output variable always comes first.
output, errors  = second_cmd.communicate()

print(output)

# call() and run() are used for small operation where there is no need to save output to a variable.
subprocess.call(['df', '-h', '/media/jamil/Data'])
subprocess.run(['df', '-h', '/media/jamil/Data'])