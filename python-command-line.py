import os
import subprocess
import shutil
from pprint import pprint
import pylint

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

f = open("/Users/georgios.kaiafas/Desktop/test_write.txt",'r',encoding = 'utf-8')
print("read the first 4 data")
f.read(4)  

print("read the next 4 data")
f.read(4)    
print("read in the rest till end of file")
f.read()   
print("further reading returns empty sting")
f.read()  
