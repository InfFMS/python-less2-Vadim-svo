n = int(input())
c = 0
for i in range(2, n):
    if i > 10:
        for l in range (2, 9):
            if i % l == 0:
                c += 1
        #print (c)
        if c == 0:
            print (i)
        c = 0
    elif i < 10:
        if i == 2 or i == 3 or i == 5 or i == 7:
            print(i)