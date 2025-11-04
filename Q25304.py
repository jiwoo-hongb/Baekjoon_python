total = int(input())
n = int(input())
sum = 0
for i in range(n):
    charge, count = map(int, input().split())
    sum += charge*count

if total == sum:
    print("Yes")
else:
    print("No")