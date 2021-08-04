from sys import argv

vigger = 0
viggest = 0
bigger = []
biggest = []
limit = int(argv[1])

def calculate(start):
    global bigger
    x = start
    next = 0
    if x % 2 != 0:
        next = (3 * x) + 1
    else:
        next = x // 2
    bigger.append(next)
    return next

results = []

def debug(num, b1, b2, v1, v2):
    print(f"# DEBUG # ")
    print(f"num: {num}")
    print(f"bigger: {len(b1)} # biggest: {len(b2)}")
    print(f"bigger: {v1} {b1}")
    print(f"biggest: {v2} {b2}")
    print("# END DEBUG #")

for i in range(1, limit + 1):
    result = i
    vigger = i
    while result > 1:
        result = calculate(result)

    debug(i, bigger, biggest, vigger, viggest)
    lbigger = len(bigger)
    lbiggest = len(biggest)

    if lbigger > lbiggest:
        biggest = []
        viggest = i
        for item in bigger:
            biggest.append(item)
    else:
        pass

    bigger = []

print(f"the number with the longest sequence is: {viggest}")
print(biggest)


