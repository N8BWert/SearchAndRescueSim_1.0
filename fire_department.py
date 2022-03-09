import re

test_file = open('test.txt', 'r')
outfile = open('addresses.txt', 'w')

file_contents = test_file.readlines()

for content in file_contents:
    print(content)
    names = re.findall('<strong>.*</strong>', content)
    x = re.findall('<br>.*<br>.*<br>', content)
    if len(names) != 0:
        for name in names:
            outfile.write(name[8:-10])
            outfile.write(',')
    if len(x) != 0:
        for string in x:
            outfile.write(string[4:-5])
            outfile.write(', Louisiana')
            outfile.write('\n')