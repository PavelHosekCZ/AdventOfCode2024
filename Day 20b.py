def bytes():  
    def printMap(l):
        for row in range(0, height):
            for col in range(0, width):
                if map[row][col] == "#":
                    print("-" * (l-1) + " ", end="")
                else:
                    print(str(map[row][col]).ljust(l), end="")
            print()  

    # load data
    with open("Day 20 input.txt", 'r') as file:
        dataInput = file.readlines()
 
    map = []

    width = len(dataInput[0].strip())
    height = len(dataInput)

    for row in dataInput:
        newRow = []
        for col in row.strip():
            newRow.append(col)
        map.append(newRow)

    printMap(2)

    for row in range(0, height):
        for col in range(0, width):
            if map[row][col] == "S": 
                map[row][col] = 0   
                startC = col
                startR = row
            if map[row][col] == "E": 
                map[row][col] = "."                               

    print("map created")

    length = 0
    row = startR
    col = startC
    while True:
        if map[row+1][col] == ".":
            map[row+1][col] = length+1
            row += 1
        elif map[row-1][col] == ".":
            map[row-1][col] = length+1
            row -= 1
        elif map[row][col+1] == ".":
            map[row][col+1] = length+1
            col += 1
        elif map[row][col-1] == ".":
            map[row][col-1] = length+1
            col -= 1
        else:
            break
        length += 1        

        
    print("basic path generated:")
    printMap(5)    
    print(f"{length}")

    # now start cheating
    row = startR
    col = startC
    skip = {}
    cheatLength = 20
    for i in range(0, length):
        for deltaY in range (-cheatLength, cheatLength + 1):
            for deltaX in range(-(cheatLength - abs(deltaY)), (cheatLength - abs(deltaY))+1):
                if 0 <= row + deltaY < height and 0 <= col + deltaX < width and isinstance(map[row+deltaY][col+deltaX], int):
                    if map[row+deltaY][col+deltaX] > i:
                        num = map[row+deltaY][col+deltaX] - i - abs(deltaY) - abs(deltaX)
                        if num > 0:
                            if num in skip:
                                skip[num] += 1
                            else:
                                skip[num] = 1


        if map[row][col-1] == i + 1:
            col -= 1
        elif map[row][col+1] == i + 1:
            col += 1
        elif map[row-1][col] == i + 1:
            row -= 1
        elif map[row+1][col] == i + 1:
            row += 1

    print(skip)

    count = 0
    for key in skip:
        if key >= 100:
            count += skip[key]
    print(f"skips saving at least 100 ps: {count} ")    




if __name__ == "__main__":
    bytes()
