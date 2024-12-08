def similarity():
    # load data into tw lists
    leftColumn = []
    rightColumn = []
    with open("Day 01 input.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        leftColumn.append(line.split()[0])
        rightColumn.append(line.split()[-1])
        
    leftColumn.sort()
    rightColumn.sort()

    frequency = {}
    for item in rightColumn:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    print("prvni cast OK")

    score = 0
    for item in leftColumn:

        if item in frequency:
            score += int(item) * frequency[item]
        
    print(score)


if __name__ == "__main__":
    similarity()
