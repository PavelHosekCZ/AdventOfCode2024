def compare():
    # load data into two lists
    leftColumn = []
    rightColumn = []
    with open("Day 01 input.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        leftColumn.append(line.split()[0])
        rightColumn.append(line.split()[-1])
        
    leftColumn.sort()
    rightColumn.sort()

    i = 0
    diff = 0
    while i < len(leftColumn):
        print(i)
        print(leftColumn[i])
        print(rightColumn[i])
        diff += abs(int(leftColumn[i]) - int(rightColumn[i]))
        i += 1

    print(diff)


if __name__ == "__main__":
    compare()
