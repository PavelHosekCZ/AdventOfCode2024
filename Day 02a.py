def similarity():
    # load data
    reports = []
    with open("Day 02 input.txt", 'r') as file:
        reports = file.readlines()

    safeCounter = 0
    for report in reports:
        levels = [int(item) for item in report.split()]
        
        i = 1
        maxIncrease = 0
        maxDecrease = 0
        changing = True
        while i < len(levels):
            change = levels[i] - levels[i-1]
            if change > maxIncrease:
                maxIncrease = change
            if change < maxDecrease:
                maxDecrease = change
            if change == 0:
                changing = False

            i += 1

        if maxDecrease * maxIncrease == 0 and maxDecrease >= -3 and maxIncrease <= 3 and changing == True:    
            safeCounter += 1
        
    print(safeCounter)


if __name__ == "__main__":
    similarity()
