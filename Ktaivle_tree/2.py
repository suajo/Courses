x = int(input())

for i in range(x+1):
    if i == 1:
        print(' '*(x-i) + '🟎')
    else:
        print(' '*(x-i) + '⁂'*(2*i-1))

print('\n')
