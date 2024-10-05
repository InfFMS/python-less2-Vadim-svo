x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 != x2) and (y1 == y2):
    print('MOZHNO')
elif (y1 != y2) and (x1 == x2):
    print('MOZHNO')
elif abs(x1 - x2) == abs(y1 - y2):
    print ('mozhno')
else:
    print('NE mozhno')