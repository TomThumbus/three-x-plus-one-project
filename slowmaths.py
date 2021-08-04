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

def produceresults(i):
    result = i
    while result > 1:
        result = calculate(result) 

if __name__ == "__main__":
    # this is the filename where the results are saved
    outfile = "output_large_4.txt"
    if len(argv) < 2:
        print("usage: python maths.py number-to-start-at")
        print("start point must be any positive number greater than four")
    else:
        max = int(argv[1])
        for i in range(1, max):
            result = i
            produceresults(result)

            big_string = f"{result}:["
            for r in results:
                big_string += str(r)
                big_string += ","
            
            results = []
            big_string += "]\n"
            f = open(outfile, 'a+')
            f.write(big_string)
            f.close()
