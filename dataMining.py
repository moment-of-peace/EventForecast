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
dictionary={}

flist = os.listdir(dirctory)  # all files in the directory
for f in flist:
    filename = dirctory + f     # file name
    src = open(filename, 'rt') # source file
    out = open('out-' + filename, 'wt') # output file
    line = src.readline().strip('\n')

    while line != '':
        columns = line.split('\t')
        for i in countryCol:
            if columns[i] == countryName: # match country
                # do something
                 
                key=columns[targetCol][0]+columns[targetCol][1]
                if key in dictionary:
                    dictionary[key]++
                else:
                    dictionary[key]=1;
        line = src.readline().strip('\n')

    src.close()
    out.close()
