a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if b1 == a2:
    print(f'[{b1}]')
elif b2 == a1:
    print(f'[{b2}]')
elif a1<=a2 and b1>=a2:
    print(f'[{a2}; {b1}]')
elif a2<=a1 and b1>=a1:
    print(f'[{a1}; {b2}]')
else:
    print('общих промежутков нет')