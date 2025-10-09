a = int(input())
b = input() # input은 str로 들어오고 str은 list처럼 사용 가능하다

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))