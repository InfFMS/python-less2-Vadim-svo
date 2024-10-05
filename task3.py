a = int(input())
if a % 10 == 1:
    print(f'{a} год')
elif a % 10 > 1 and a % 10 < 5:
    print(f'{a} гойда')
elif a % 10 > 4 or a % 10 == 0:
    print(f'{a} лет')