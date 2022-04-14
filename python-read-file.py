f = open("/Users/georgios.kaiafas/Desktop/test_file.txt", "a")
f.writelines("This line is appended to the txt file")
f.close()

f = open("/Users/georgios.kaiafas/Desktop/test_file.txt", "r")
print(f"We print all the lines of the txt file")
print(f.readlines())
f.close()


print(f"We print all the lines of the txt file - line by line with a for loop")
with open('/Users/georgios.kaiafas/Desktop/test_file.txt') as sample: 
    for line in sample:
        print(line.rstrip()) 