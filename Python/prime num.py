# 소수 찾기


def is_prime_num(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


print(is_prime_num(5))
print(is_prime_num(8))

# --------------------------
# import math


# def is_prime_num(x):
#     # 2부터 x의 '제곱근'까지의 모든 수 확인
#     for i in range(2, int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False

#     return True


# print(is_prime_num(5))
# print(is_prime_num(8))
