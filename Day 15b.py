def sokoban():
    def printMap():
        for row in range(0, height):
            for col in range(0, width):
                print(map[row][col], end="")
            print()

    def canBoxBeMoved(direction, row, col):
        # can box at [row, col] be moved in the [direction]?
        if map[row][col] == "]":
            col -= 1

        match instruction:
            case "^":
                if map[row-1][col] == "#" or map[row-1][col+1] == "#":
                    return False                
                if map[row-1][col] == "." and map[row-1][col+1] == ".":
                    return True
                if map[row-1][col] == "[" :
                    return canBoxBeMoved(direction, row-1, col)
                if map[row-1][col] == "]" and map[row-1][col+1] == ".":
                    return canBoxBeMoved(direction, row-1, col)
                if map[row-1][col] == "]" and map[row-1][col+1] == "[":
                    return canBoxBeMoved(direction, row-1, col) * canBoxBeMoved(direction, row-1, col+1)
                if map[row-1][col] == "." and map[row-1][col+1] == "[":
                    return canBoxBeMoved(direction, row-1, col+1)                
                
            case "v":
                if map[row+1][col] == "#" or map[row+1][col+1] == "#":
                    return False                
                if map[row+1][col] == "." and map[row+1][col+1] == ".":
                    return True
                if map[row+1][col] == "[" :
                    return canBoxBeMoved(direction, row+1, col)
                if map[row+1][col] == "]" and map[row+1][col+1] == ".":
                    return canBoxBeMoved(direction, row+1, col)
                if map[row+1][col] == "]" and map[row+1][col+1] == "[":
                    return canBoxBeMoved(direction, row+1, col) * canBoxBeMoved(direction, row+1, col+1)
                if map[row+1][col] == "." and map[row+1][col+1] == "[":
                    return canBoxBeMoved(direction, row+1, col+1)  
                
            case "<":
                if map[row][col-1] == ".":
                    return True
                if map[row][col-1] == "#":
                    return False
                if map[row][col-1] == "]":
                    return canBoxBeMoved(direction, row, col-1)
            case ">":
                if map[row][col+2] == ".":
                    return True
                if map[row][col+2] == "#":
                    return False
                if map[row][col+2] == "[":
                    return canBoxBeMoved(direction, row, col+2)
                

    def moveBox(direction, row, col):
        # move box at [row, col] in the [direction]
        if map[row][col] == "]":
            col -= 1

        match instruction:
            case "^":
                if map[row-1][col] == "]" or map[row-1][col] == "[":
                    moveBox(direction, row-1, col)
                if map[row-1][col+1] == "[" :
                    moveBox(direction, row-1, col+1)
                map[row][col] = "."
                map[row][col+1] = "."
                map[row-1][col] = "["  
                map[row-1][col+1] = "]"  
            case "v":
                if map[row+1][col] == "]" or map[row+1][col] == "[":
                    moveBox(direction, row+1, col)
                if map[row+1][col+1] == "[" :
                    moveBox(direction, row+1, col+1)
                map[row][col] = "."
                map[row][col+1] = "."
                map[row+1][col] = "["  
                map[row+1][col+1] = "]"  
            case "<":
                if map[row][col-1] == "]":
                    moveBox(direction, row, col-1)
                map[row][col-1] = "["
                map[row][col] = "]"
                map[row][col+1] = "."                    
            case ">":
                if map[row][col+2] == "[":
                    moveBox(direction, row, col+2)                  
                map[row][col] = "."
                map[row][col+1] = "["
                map[row][col+2] = "]"
              


    # load data
    datadataInput = []
    with open("Day 15 input.txt", 'r') as file:
        dataInput = file.readlines()
    
    width = len(dataInput[0].strip())*2
    map = []
    dataInputLen = len(dataInput)

    i = 0
    while dataInput[i] != "\n":
        row=[]
        for col in dataInput[i].strip():
            match col:
                case "#":
                    row.append("#")
                    row.append("#")
                case "O":
                    row.append("[")
                    row.append("]")
                case ".":
                    row.append(".")
                    row.append(".")
                case "@":
                    row.append("@")
                    row.append(".")
        map.append(row)
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
                        elif map[R-1][C] == "[" or map[R-1][C] == "]":
                            if canBoxBeMoved("^", R-1, C):  
                                moveBox("^", R-1, C)
                                map[R][C] = "."
                                map[R-1][C] = "@"
                                R -= 1                            
                case "v":
                    if R < height - 1:
                        if map[R+1][C] == ".":
                            map[R][C] = "."
                            map[R+1][C] = "@"
                            R += 1
                        elif map[R+1][C] == "[" or map[R+1][C] == "]":
                            if canBoxBeMoved("v", R+1, C):  
                                moveBox("v", R+1, C)
                                map[R][C] = "."
                                map[R+1][C] = "@"
                                R += 1                            
                case "<":
                    if C > 0:
                        if map[R][C-1] == ".":
                            map[R][C] = "."
                            map[R][C-1] = "@"
                            C -= 1
                        elif map[R][C-1] == "]":
                            if canBoxBeMoved("<", R, C-1):  
                                moveBox("<", R, C-1)                          
                                map[R][C] = "."
                                map[R][C-1] = "@"
                                C -= 1                             
                case ">":
                    if C < width - 1:
                        if map[R][C+1] == ".":
                            map[R][C] = "."
                            map[R][C+1] = "@"
                            C += 1
                        elif map[R][C+1] == "[":
                            if canBoxBeMoved(">", R, C+1): 
                                moveBox(">", R, C+1)                           
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
            if map[row][col] == "[":
                count += row * 100 + col

    printMap()
    print(f"count: {count}")

if __name__ == "__main__":
    sokoban()
