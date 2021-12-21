num = 0
tot = 0.0
while Ture:
    sval = input('Enter a number:')
    if sval == 'done':
        break
    try:  # 에러 방지
        fval = float(sval)
    except:
        print('Invalid input')
        continue  # 잘못된 데이터 제외 루프 재실행
    # print(fval)
    num = num + 1  # 개수 세기 패턴
    tot = tot + fval  # 합계 구하기 패턴

print('ALL DONE')
print(tot, num, tot/num)
