hour, min = map(int, input().split())

new_hour, new_min = 0, 0

if min - 45 >= 0:
    new_hour = hour
    new_min = min - 45
elif min - 45 < 0:
    if hour == 0:
        new_hour = 23
    else: new_hour = hour - 1
    new_min = (60+min)- 45

print(new_hour, new_min)
     