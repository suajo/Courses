fhand = open('d:/조수아/08 DX/TIL/Python/01_py4e_ex/mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    wds = line.split()
    # Guardian pattern
    if len(wds) < 1:
        continue
    if wds[0] != 'From':
        continue
    print(wds[2])
