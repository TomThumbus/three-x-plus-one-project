numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def longest_line():
    with open("output_large_3.txt", 'r') as f:
        out = ""
        largest = 0
        for line in f:
            if len(line) > largest:
                largest = len(line)
                out = line
        
    print(line)

def most_derivatives():
    count = 0
    highest = 0
    most = []
    with open("output_large_3.txt", 'r') as f:
        for line in f:
            count = 0
            for c in line:
                if c == ",":
                    count += 1

            if count > highest:
                most = []
                most.append(line)
            elif count == highest:
                most.append(line)
            else:
                pass
    
    for m in most:
        print(m)



most_derivatives()


