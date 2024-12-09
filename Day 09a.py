def defrag():
    # load data
    input = []
    with open("Day 09 input.txt", 'r') as file:
        input = file.readlines()
    rawSequence = input[0].strip()
    
    #print("input:")
    #print(rawSequence)
    print("input loaded")
    
    sequence = []
    i = 0
    printItem = True # switches between writing blocks and spaces
    for item in rawSequence:
        if printItem == True:
            for j in range(0, int(item)):
                sequence.append(i)
            i += 1
            printItem = False
        else:
            for j in range(0, int(item)):
                sequence.append(".")
            printItem = True
    
    #print("sequence:")
    #print(sequence)
    print("sequence created")

    for i in range(len(sequence)-1, 0, -1):
        print(i)
        if sequence[i] == ".":
            continue
        # i is last element, we want to move it to first available gap
        gap = len(sequence)
        for j in range(0, i):
            if sequence[j] == ".":
                gap = j
                break
        if gap == len(sequence):
            break

        sequence[gap], sequence[i] = sequence[i], sequence[gap]
        #print(sequence)

    count = 0

    for i in range(0, len(sequence)):
        if sequence[i] == ".":
            break
        count += i * sequence[i]

    print(f"count: {count}")

if __name__ == "__main__":
    defrag()
