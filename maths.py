from sys import argv

results = []

def calculate(start):
    global results
    x = start
    next = 0
    if x % 2 != 0:
        next = (3 * x) + 1
    else:
        next = x // 2
    results.append(next)
    #print(next)
    return next

if __name__ == "__main__":
    if len(argv) < 2:
        print("usage: python maths.py number-to-start-at")
        print("start point must be any positive number greater than four")
    else:
        result = int(argv[1])
        while result > 1:
            result = calculate(result)
        
        print(results)
