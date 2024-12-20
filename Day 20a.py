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
    for i in range(0, length):
        if row < height - 2 and map[row+1][col] == "#" and isinstance(map[row+2][col], int):
            if map[row+2][col] > i:
                num = map[row+2][col] - i - 2
                if num in skip:
                    skip[num] += 1
                else:
                    skip[num] = 1
        if row > 1 and map[row-1][col] == "#" and isinstance(map[row-2][col], int):
            if map[row-2][col] > i:
                num = map[row-2][col] - i - 2
                if num in skip:
                    skip[num] += 1
                else:
                    skip[num] = 1
        if col < width - 2 and map[row][col+1] == "#" and isinstance(map[row][col+2], int):
            if map[row][col+2] > i:
                num = map[row][col+2] - i - 2
                if num in skip:
                    skip[num] += 1
                else:
                    skip[num] = 1
        if col > 1 and map[row][col-1] == "#" and isinstance(map[row][col-2], int):
            if map[row][col-2] > i:
                num = map[row][col-2] - i - 2
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
