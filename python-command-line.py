import os
import subprocess
import shutil
from pprint import pprint

# Get your current working directly
# This returns a string
my_cwd = os.getcwd()
print(my_cwd)

print("\nContents of the current directory")
# List the contents of a directory
# This returns a list
dir_list = os.listdir()
for item in dir_list:
    print(item)


print("\nRead Write files")
file = open("/Users/georgios.kaiafas/Desktop/test_file.txt","r")
print(f"4th line of the txt file is: {file.read(3)}")
file.close()
