def defrag():
    # load data
    input = []
    with open("Day 09 input.txt", 'r') as file:
        input = file.readlines()
    rawSequence = input[0].strip()

    sequence = []
    lengths = []
    positions = []
    i = 0
    printItem = True # switches between writing blocks and spaces
    for item in rawSequence:
        if printItem == True:
            positions.append(len(sequence))
            for j in range(0, int(item)):
                sequence.append(i)
            i += 1
            lengths.append(int(item))
            printItem = False
        else:
            for j in range(0, int(item)):
                sequence.append(".")
            printItem = True
       

    l = len(sequence)

    for item in range(len(lengths)-1,0,-1):
        print(item)
        i = 0
        spaceLen = 0
        while i < positions[item]:
            if sequence[i] == ".":
                spaceLen += 1
            else:
                spaceLen = 0
            if spaceLen == lengths[item]:
                print(f"found gap long {spaceLen} at position {i} / {l}")
                break
            i += 1

        if i < positions[item]:
            for value in range(sequence.index(item), sequence.index(item)+lengths[item]):
                sequence[value] = "."
            for value in range(i-lengths[item]+1, i+1):
                sequence[value] = item
            positions[item] = i-lengths[item]+1   

    count = 0

    for i in range(0, len(sequence)):
        if sequence[i] != ".":
            count += i * sequence[i]

    print(f"count: {count}")

if __name__ == "__main__":
    defrag()
