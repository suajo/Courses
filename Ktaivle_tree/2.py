x = int(input())

print('\n'*2)

for i in range(x+1):
    if i == 1:
        print(' '*5 + ' '*(x-i) + '🟎')
    else:
        print(' '*5 + ' '*(x-i) + '⁂'*(2*i-1))

print('\n'*2)
