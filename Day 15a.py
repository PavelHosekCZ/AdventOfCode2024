def sokoban():
    def printMap():
        for row in range(0, height):
            for col in range(0, width):
                print(map[row][col], end="")
            print()

    def addBox(direction, row, col):
        if map[row][col] == ".":
            map[row][col] = "O"
            return True
        if map[row][col] == "#":
            return False
        # not "." nor "#" > we must be on another O
        # the map seems to be bordred by #, we can omit checking if we're in the range of map
        match instruction:
            case "^":
                return addBox("^", row-1, col)
            case "v":
                return addBox("^", row+1, col)
            case "<":
                return addBox("<", row, col-1)
            case ">":
                return addBox(">", row, col+1)

    # load data
    datadataInput = []
    with open("Day 15 input.txt", 'r') as file:
        dataInput = file.readlines()
    
    width = len(dataInput[0].strip())
    map = []
    dataInputLen = len(dataInput)

    i = 0
    while dataInput[i] != "\n":
        map.append([col for col in dataInput[i].strip()])
        i += 1

    height = i
    printMap()

    for row in range(0, height):
        for col in range(0, width):
            if map[row][col] == "@":
                C = col
                R = row

    print(f"{R=}, {C=}")
    print("starting to move the robot")

    # Move the robot through the map
    i += 1
    while i < dataInputLen:
        instructions = dataInput[i].strip()
        for instruction in instructions:
            match instruction:
                case "^":
                    if R > 0:
                        if map[R-1][C] == ".":
                            map[R][C] = "."
                            map[R-1][C] = "@"
                            R -= 1
                        elif map[R-1][C] == "O":
                            if addBox("^", R-1, C):
                                map[R][C] = "."
                                map[R-1][C] = "@"
                                R -= 1                            
                case "v":
                    if R < height - 1:
                        if map[R+1][C] == ".":
                            map[R][C] = "."
                            map[R+1][C] = "@"
                            R += 1
                        elif map[R+1][C] == "O":
                            if addBox("v", R+1, C): 
                                map[R][C] = "."
                                map[R+1][C] = "@"
                                R += 1                            
                case "<":
                    if C > 0:
                        if map[R][C-1] == ".":
                            map[R][C] = "."
                            map[R][C-1] = "@"
                            C -= 1
                        elif map[R][C-1] == "O":
                            if addBox("<", R, C-1):                            
                                map[R][C] = "."
                                map[R][C-1] = "@"
                                C -= 1                             
                case ">":
                    if C < width - 1:
                        if map[R][C+1] == ".":
                            map[R][C] = "."
                            map[R][C+1] = "@"
                            C += 1
                        elif map[R][C+1] == "O":
                            if addBox(">", R, C+1):                            
                                map[R][C] = "."
                                map[R][C+1] = "@"
                                C += 1     
            #print(instruction)
            #printMap()
            #print()

        i += 1


    count = 0
    for row in range(0, height):
        for col in range(0, width):
            if map[row][col] == "O":
                count += row * 100 + col

    printMap()
    print(f"count: {count}")

if __name__ == "__main__":
    sokoban()
