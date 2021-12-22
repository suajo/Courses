x = int(input())
# x > 5

print('\n'*2)

for i in range(x+1):
    if i == 1:
        print(' '*5 + ' '*(x-i) + '🟎')
    elif i % 5 == 0:
        print(' '*5 + ' '*(x-(i-1)) + '⋆'*(2*(i-1)))
    else:
        print(' '*5 + ' '*(x-i) + '⁂'*(2*i-1))
for k in range(2):
    print(' '*(x+2) + '│││││')

print('\n'*8)
