x = int(25)

print('\n'*2)

for i in range(8):
    if i == 1:
        print(' '*10 + ' '*(x-i) + '\u001b[33mð')
    elif i % 4 == 0:
        print(' '*10 + ' '*(x-(i-1)) + '\u001b[33mâ'*(2*(i-1)))
    else:
        print(' '*10 + ' '*(x-i) + '\u001b[32mâ'*(2*i-1))
for i in range(8, 16):
    if i == 1:
        print(' '*10 + ' '*(x-i) + '\u001b[33mð')
    elif i % 4 == 0:
        print(' '*10 + ' '*(x-(i-1)+3) + '\u001b[33mâ'*(2*(i-1-3)))
    else:
        print(' '*10 + ' '*(x-i+3) + '\u001b[32mâ'*(2*i-1-6))
for i in range(16, x+1):
    if i == 1:
        print(' '*10 + ' '*(x-i) + '\u001b[33mð')
    elif i % 4 == 0:
        print(' '*10 + ' '*(x-(i-1)+6) + '\u001b[33mâ'*(2*(i-1-6)))
    else:
        print(' '*10 + ' '*(x-i+6) + '\u001b[32mâ'*(2*i-1-12))

for k in range(3):
    print(' '*(x+7) + '\u001b[37mâââââ')

print('ï¿£'*35)

print('\n'*8)
