fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'd:/조수아/08 DX/TIL/Python/01_py4e_ex/clown.txt'
fhand = open(fname)

di = dict()
for line in fhand:
    line = line.rstrip()
    # print(line)
    wds = line.split()
    # print(wds)
    for w in wds:
        # if the key is not there the count is zero
        #oldcount = di.get(w, 0)
        #print(w, 'old', oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount

        # idiom : retrieve/create/update counter
        di[w] = di.get(w, 0) + 1
        #print(w, 'new', di[w])
        #print(w, di[w])
# print(di)

# now we want to find the most common word
largest = -1
theword = None
for key, val in di.items():
    print(key, val)
    if val > largest:
        largest = val
        theword = key  # capture/remember the word that was largest

print('Done', theword, largest)
