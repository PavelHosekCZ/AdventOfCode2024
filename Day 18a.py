def bytes():
    iter = [0]     
    def printMap(l):
        for row in range(0, height):
            for col in range(0, width):
                if map[row][col] == "#":
                    print("-" * (l-1) + " ", end="")
                else:
                    print(str(map[row][col]).ljust(l), end="")
            print()   


    # load data
    with open("Day 18 input.txt", 'r') as file:
        dataInput = file.readlines()

    width = 71 # as stated in the assignment; 71 main task, 7 example
    height = 71 # as stated in the assignment; 71 main task, 7 example
   
    map = []

    for row in range(0, height):
        newRow = []
        for col in range(0, width):
            newRow.append(".")
        map.append(newRow)

    i = 0
    for byte in dataInput:
        col,row = byte.strip().split(",")
        map[int(row)][int(col)] = "#"
        i+=1
        if i == 1024: # as stated in the assignment; 1024 main task, 12 example
            break

    printMap(2)

    map[0][0] = 0

    i = 0
    while True:
        modded = False
        for r in range(0, height):
            for c in range(0, width):
                if map[r][c] != "#":
                    if r>0 and isinstance(map[r-1][c], int):
                        T = map[r-1][c]
                    else:
                        T = "?"
                    if r<height-1 and isinstance(map[r+1][c], int):
                        B = map[r+1][c]
                    else:
                        B = "?"
                    if c>0 and isinstance(map[r][c-1], int):
                        L = map[r][c-1]
                    else:
                        L = "?"
                    if c<width-1 and isinstance(map[r][c+1], int):
                        R = map[r][c+1]
                    else:
                        R = "?"
                    if L != "?" or R != "?" or T != "?" or B != "?":
                        if isinstance(L, int):
                            lowestNeighbour = L
                        if isinstance(R, int):
                            lowestNeighbour = R
                        if isinstance(T, int):
                            lowestNeighbour = T
                        if isinstance(B, int):
                            lowestNeighbour = B
                        if isinstance(L, int) and L < lowestNeighbour:
                            lowestNeighbour = L
                        if isinstance(R, int) and R < lowestNeighbour:
                            lowestNeighbour = R
                        if isinstance(T, int) and T < lowestNeighbour:
                            lowestNeighbour = T
                        if isinstance(B, int) and B < lowestNeighbour:
                            lowestNeighbour = B                  
                        if map[r][c] == ".":
                            map[r][c] = lowestNeighbour + 1
                            modded = True
                        elif map[r][c] > lowestNeighbour + 1:
                            map[r][c] = lowestNeighbour + 1
                            modded = True
        if i % 100000 == 0:
            printMap(4)
            print
        i += 1
        if modded == False:
            break


    print(f"FINALE, {i=}")
    printMap(4)    
    print(f"count: {map[height-1][width-1]}")

if __name__ == "__main__":
    bytes()
