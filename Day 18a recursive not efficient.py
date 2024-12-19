def bytes():
    iter = [0]     
    def printMap(l):
        for row in range(0, height):
            for col in range(0, width):
                print(str(map[row][col]).ljust(l), end="")
            print()

    def walk(r, c, w):
        if isinstance(map[r][c], int) and w > map[r][c]:
            return

        map[r][c] = w

        if r > 0 and map[r-1][c] != "#":
            walk(r-1, c, w+1)
        if r < height-1 and map[r+1][c] != "#":
            walk(r+1, c, w+1)            
        if c > 0 and map[r][c-1] != "#":
            walk(r, c-1, w+1)            
        if c < width-1 and map[r][c+1] != "#":
            walk(r, c+1, w+1)       

        iter[0] = iter[0] + 1
        if iter[0] % 1000000 == 0:
            printMap(5)     


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



    # optimise the map
    while True:
        modded = False
        for row in range(0, height):
            for col in range(0, width):
                # get map of surroundings
                LT = "#"
                T = "#"
                RT = "#"
                L = "#"
                R = "#"
                LB = "#"
                B = "#"
                RB = "#"
                if row > 0:
                    if col > 0 and map[row-1][col-1] == ".":
                        LT = "."
                    if map[row-1][col] == ".":
                        T = "."
                    if col < width - 1 and map[row-1][col+1] == ".":
                        RT = "."
                if col > 0 and map[row][col-1] == ".":
                    L = "."
                if col < width - 1 and map[row][col+1] == ".":
                    R = "."
                if row < height - 1:
                    if col > 0 and map[row+1][col-1] == ".":
                        LB = "."
                    if map[row+1][col] == ".":
                        B = "."
                    if col < width - 1 and map[row+1][col+1] == ".":
                        RB = "."

                # dead ends
                if T == "#" and L == "#" and B == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # >
                    map[row][col] = "#"
                    modded = True
                if T == "#" and R == "#" and B == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # <
                    map[row][col] = "#"
                    modded = True                    
                if B == "#" and L == "#" and R == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # ^
                    map[row][col] = "#"
                    modded = True                    
                if R == "#" and L == "#" and T == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2  : # v
                    map[row][col] = "#"
                    modded = True     

                # caves
                if T == "#" and B == "#" and L == "#" and R == "#" and map[row][col] == "." : # >
                    map[row][col] = "#"
                    modded = True    

                # empty corners
                if L == "." and T == "." and LT == "." and R == "#" and B == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # bypass at top left
                    map[row][col] = "#"
                    modded = True
                if L == "#" and T == "." and RT == "." and R == "." and B == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # bypass at top right
                    map[row][col] = "#"
                    modded = True
                if L == "." and B == "." and LB == "." and R == "#" and T == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # bypass at bottom left
                    map[row][col] = "#"
                    modded = True
                if L == "#" and T == "#" and RB == "." and R == "." and B == "." and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # bypass at bottom right
                    map[row][col] = "#"
                    modded = True

                # # long sides CAREFUL! changes length of the travelled path!
                # if L == LT == LB == T == B == "." and RT == R == RB == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # empty left side
                #     map[row][col] = "#"
                #     modded = True
                # if R == RT == RB == T == B == "." and LT == L == LB == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # empty right side
                #     map[row][col] = "#"
                #     modded = True
                # if T == LT == RT == L == R == "." and LB == B == RB == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # empty top side
                #     map[row][col] = "#"
                #     modded = True
                # if B == LB == RB == L == R == "." and LT == T == RT == "#" and map[row][col] == "." and row + col > 0 and row + col < width + height - 2 : # empty top side
                #     map[row][col] = "#"
                #     modded = True                    

        if modded == False:
            break

    print()
    printMap(2) 

    walk(0, 0, 0)

    print()
    printMap(2)    
    
    print(f"count: {map[height-1][width-1]}")

if __name__ == "__main__":
    bytes()
