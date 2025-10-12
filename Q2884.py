hour, min = map(int, input().split())

new_hour, new_min = 0, 0

if (hour - 1 >= 0) and (min - 45 >= 0):
    new_hour = hour - 1
    new_min = min - 45