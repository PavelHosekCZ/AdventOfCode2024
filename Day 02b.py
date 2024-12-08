def similarity():
    # load data
    reports = []
    with open("Day 02 input.txt", 'r') as file:
        reports = file.readlines()

    safeCounter = 0
    for report in reports:
        levels = [int(item) for item in report.split()]
        removeItemID = -1            
        while removeItemID < len(levels):
            i = 1
            if removeItemID >= 0:
                levels_modified = levels.copy()
                levels_modified.pop(removeItemID)
            else:
                levels_modified = levels.copy()              
            maxIncrease = 0
            maxDecrease = 0
            changing = True            
            while i < len(levels_modified):
                change = levels_modified[i] - levels_modified[i-1]
                if change > maxIncrease:
                    maxIncrease = change
                if change < maxDecrease:
                    maxDecrease = change
                if change == 0:
                    changing = False
                i += 1

            if maxDecrease * maxIncrease == 0 and maxDecrease >= -3 and maxIncrease <= 3 and changing == True:    
                safeCounter += 1
                break

            removeItemID += 1      
        
    print(safeCounter)


if __name__ == "__main__":
    similarity()
