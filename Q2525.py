hour, min = map(int, input().split())
time = int(input())

new_hour, new_min = 0, 0

new_min = min + time

if new_min < 60:
    new_hour = hour
    new_min = new_min
elif new_min >= 60:
    new_hour = hour + (new_min // 60) 
    new_min = new_min % 60
    if new_hour >= 24:
        new_hour = (new_hour%24)

print(new_hour, new_min)