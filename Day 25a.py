def lockpicking():  
    # load data
    with open("Day 25 input.txt", 'r') as file:
        data = file.readlines()
    locks = []
    keys = []
    length = len(data[0].strip())
    height = 7 # hardcoded height of lock / key pattern
    i = 0
    # loop over all lines of input (row index "i"):
    while i < len(data):
        pattern = []
        # iterate each lock / key left to right (column index "j"): 
        for j in range(0, length):
            sum = -1
            for k in range(i, i+height):
                if data[k][j] == "#":
                    sum += 1
            pattern.append(sum)
        if data[i].strip() == "#####":
            locks.append(pattern)
        else:
            keys.append(pattern)
        i += height+1

    #print(f"{keys=}")
    #print(f"{locks=}")
    #print(f"{len(keys)=}, {len(locks)=}")

    pairCount = 0
    for lock in locks:
        for key in keys:
            fits = True
            for pin in range(0, length):
                if lock[pin] + key[pin] > height - 2:
                    fits = False
                    break
            if fits == True:
                pairCount += 1
    
    print(f"Possible unique lock-key pairs: {pairCount}")
        



if __name__ == "__main__":
    lockpicking()
