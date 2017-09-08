'''
Attribute counter
For a given attribute indicated by 'targetCol', count how many times each value appears and
write the result in a file
Output foramt:
countryName targetCol
value1 number1
value2 number2
...... ......

'''
import os

dirctory = ''
countryCol = [36] # the column index of country name
countryName = 'Australia' # the country to be extracted
targetCol = 0

flist = os.listdir(dirctory)  # all files in the directory
for f in flist:
    filename = dirctory + f     # file name
    src = open(filename, 'rt') # source file
    out = open('out-' + filename, 'wt') # output file
    line = src.readline().strip('\n')

    while line != '':
        for i in countryCol:
            if columns[i] == countryName: # match country
                # do something
        line = src.readline().strip('\n')

    src.close()
    out.close()
