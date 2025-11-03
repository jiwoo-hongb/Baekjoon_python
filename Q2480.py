a, b, c = map(int, input().split())

if (a == b and b == c):
    print(10000+a*1000)
elif (a == b or a == c):
    print(1000+a*100)
elif (b == c):
    print(1000+c*100)
else:
    if (a > b and a > c):
        print(a*100)
    elif (b > c and b > a):
        print(b*100)
    elif (c > b and c > a):
        print(c*100)