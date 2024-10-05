a = int(input())
if a < 5:
    hrs = 7 + a
    min = 30 - (a-1) * 5
    print (f'{hrs}:{min}---{hrs+1}:{min-15}')
elif a >= 5:
    hrs = 7+a
    min = 50 - (a-1) * 5
    print (f'{hrs}:{min}---{hrs+1}:{min-15}')