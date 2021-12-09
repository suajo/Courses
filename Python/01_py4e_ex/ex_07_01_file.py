fhand = open('mbox-short.txt', 'r')

for line in fhand:
    line = line.rstrip()
    print(line.upper())
