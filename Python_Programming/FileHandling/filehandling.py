"""Creating and Writing a file"""
# Approach 1
file = open('E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\myfile.txt', 'w')
file.write('Welcome to python world \nFile handling concept')
file.close()


# Approach 2 : using with keyword
with open('E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\myfile1.txt', 'w') as file:
    file.write('Welcome to python world \nFile handling concept---11')
    file.close()

'''Appending data into file'''
file = open('E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\myfile1.txt', 'a')
file.write('\nThis new file/line is appended')
file.close()



'''Reading data from text file'''
'''
read() = reads entire data
readline() = read single line
readlines() = read all the lines into list format
'''
file = open('E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\myfile1.txt', 'r')
#content = file.read()
#content = file.readline()
content = file.readlines()

print(content)


# Rename the file
# import os
# os.rename('E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\myfile2.txt', 'E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\myfile_renamed.txt')
#
# print('File renamed...')


# Delete the file
import os
file = 'E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\myfile1.txt'

if os.path.exists(file):
    os.remove(file)
    print('File deleted')
else:
    print('File does not match')


# Creating a directory/folder
# import os
# os.mkdir('E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\mydir123')
# print('directory created')

# check the directory exist or not
import os
mydir = 'E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\mydir'

if os.path.exists(mydir):
    print('directory exists')
else:
    print('directory does not match')


# Rename the directory
# import os
# os.rename('E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\mydir', 'E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\mydir_11')
# print('Directory renamed')


# Remove the directory
# import os
# import shutil   # Another method to remove the directory
# os.rmdir('E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\mydir123')
# shutil.rmtree('E:\\Automation_Scripts\\PyCharm\\Python_Coding\\Python_Programming\\FileHandling\\mydir123') # perform is the file exists
# print('directory removed')


# Get the current working directory
import os
print(os.getcwd())

















