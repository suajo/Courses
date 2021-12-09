fhand = open('d:/조수아/08 DX/TIL/Python/01_py4e_ex/mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    print(line.upper())
