fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'd:/조수아/08 DX/TIL/Python/01_py4e_ex/clown.txt'
fhand = open(fname)

di = dict()
for line in fhand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1

# print(di)

tmp = list()
for k, v in di.items():
    # print(k,v)
    newt = (v, k)
    tmp.append(newt)

# print('Flipped', tmp)
tmp = sorted(tmp, reverse=True)
# print('Sorted', tmp[:5])

for v, k in tmp[:5]:
    print(k, v)
