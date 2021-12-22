x = int(18)

print('\n'*2)

for i in range(x+1):
    if i == 1:
        print(' '*5 + ' '*(x-i) + '\u001b[33m🟎')
    elif i % 4 == 0:
        print(' '*5 + ' '*(x-(i-1)) + '\u001b[33m⋆'*(2*(i-1)))
    else:
        print(' '*5 + ' '*(x-i) + '\u001b[32m⁂'*(2*i-1))
for k in range(3):
    print(' '*(x+2) + '\u001b[37m│││││')

print('￣'*23)

print('\n'*8)
