marks = [92, 42, 24, 71, 83]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d 축하"%number)
