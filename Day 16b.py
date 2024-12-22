def maze():
    def printMap():
        l = 6
        for row in range(0, height):
            for col in range(0, width):
                if map[row][col] == "#":
                    print("#" * (l * 4 - 1), end=" ")
                elif map[row][col] == "O":
                    print("O" * (l * 4 - 1), end=" ")                   
                elif map[row][col] == {}:
                    print("." * (l * 4 - 1), end=" ")                    
                else:
                    toTop = "." * (l-1) + " "
                    toBottom = "." * (l-1) + " "
                    toLeft = "." * (l-1) + " "
                    toRight = "." * (l-1) + " "
                    if isinstance(map[row][col], dict) and ">" in map[row][col] and isinstance(map[row][col][">"], int):
                        toRight = str(map[row][col][">"]).ljust(l)
                    if isinstance(map[row][col], dict) and "<" in map[row][col] and isinstance(map[row][col]["<"], int):
                        toLeft = str(map[row][col]["<"]).ljust(l)
                    if isinstance(map[row][col], dict) and "v" in map[row][col] and isinstance(map[row][col]["v"], int):
                        toBottom = str(map[row][col]["v"]).ljust(l)
                    if isinstance(map[row][col], dict) and "^" in map[row][col] and isinstance(map[row][col]["^"], int):
                        toTop = str(map[row][col]["^"]).ljust(l)
                    print(toLeft + toTop + toBottom + toRight, end="")
            print()  

    # load data
    with open("Day 16 input.txt", 'r') as file:
        dataInput = file.readlines()

    width = len(dataInput[0].strip())
    height = len(dataInput)
    map = []

    for row in dataInput:
        map.append([col for col in row.strip()])

    for row in range(0, height):
        for col in range(0, width):
            if map[row][col] == "S":
                startC = col
                startR = row
                map[row][col] = {">" : 1, "v" : 1001, "^" : 1001, "<" : 2001}
            if map[row][col] == "E":
                endC = col
                endR = row
                map[row][col] = {}
            if map[row][col] == ".":
                map[row][col] = {}

    while True:
        change = False
        for row in range(0, height):
            for col in range(0, width):
                if map[row][col] == "#":
                    continue
                fromTop = "."
                fromBottom = "."
                fromLeft = "."
                fromRight = "."
                if isinstance(map[row][col-1], dict) and ">" in map[row][col-1] and isinstance(map[row][col-1][">"], int):
                    fromLeft = map[row][col-1][">"]
                if isinstance(map[row][col+1], dict) and "<" in map[row][col+1] and isinstance(map[row][col+1]["<"], int):
                    fromRight = map[row][col+1]["<"]
                if isinstance(map[row-1][col], dict) and "v" in map[row-1][col] and isinstance(map[row-1][col]["v"], int):
                    fromTop = map[row-1][col]["v"]
                if isinstance(map[row+1][col], dict) and "^" in map[row+1][col] and isinstance(map[row+1][col]["^"], int):
                    fromBottom = map[row+1][col]["^"]
                # new ">"
                new = []
                if isinstance(fromLeft, int):
                    new.append(fromLeft+1)
                if isinstance(fromTop, int):
                    new.append(fromTop+1001)
                if isinstance(fromBottom, int):
                    new.append(fromBottom+1001)
                if isinstance(fromRight, int):
                    new.append(fromRight+2001)
                if new != []:
                    newValue = min(new)
                    if ((">" in map[row][col] and newValue < map[row][col][">"])) or (">" not in map[row][col]):
                        map[row][col][">"] = newValue
                        change = True
                # new "<"
                new = []
                if isinstance(fromLeft, int):
                    new.append(fromLeft+2001)
                if isinstance(fromTop, int):
                    new.append(fromTop+1001)
                if isinstance(fromBottom, int):
                    new.append(fromBottom+1001)
                if isinstance(fromRight, int):
                    new.append(fromRight+1)
                if new != []:
                    newValue = min(new)
                    if (("<" in map[row][col] and newValue < map[row][col]["<"])) or ("<" not in map[row][col]):
                        map[row][col]["<"] = newValue
                        change = True       
                # new "^"
                new = []
                if isinstance(fromLeft, int):
                    new.append(fromLeft+1001)
                if isinstance(fromTop, int):
                    new.append(fromTop+2001)
                if isinstance(fromBottom, int):
                    new.append(fromBottom+1)
                if isinstance(fromRight, int):
                    new.append(fromRight+1001)
                if new != []:
                    newValue = min(new)
                    if (("^" in map[row][col] and newValue < map[row][col]["^"])) or ("^" not in map[row][col]):
                        map[row][col]["^"] = newValue
                        change = True       
                # new "v"
                new = []
                if isinstance(fromLeft, int):
                    new.append(fromLeft+1001)
                if isinstance(fromTop, int):
                    new.append(fromTop+1)
                if isinstance(fromBottom, int):
                    new.append(fromBottom+2001)
                if isinstance(fromRight, int):
                    new.append(fromRight+1001)
                if new != []:
                    newValue = min(new)
                    if (("v" in map[row][col] and newValue < map[row][col]["v"])) or ("v" not in map[row][col]):
                        map[row][col]["v"] = newValue
                        change = True                                                                

        if change == False:
            break

    print(f"{endR=}, {endC=}")

    row = endR
    col = endC
    fromTop = "."
    fromBottom = "."
    fromLeft = "."
    fromRight = "."    
    if isinstance(map[row][col-1], dict) and ">" in map[row][col-1] and isinstance(map[row][col-1][">"], int):
        fromLeft = map[row][col-1][">"]
    if isinstance(map[row][col+1], dict) and "<" in map[row][col+1] and isinstance(map[row][col+1]["<"], int):
        fromRight = map[row][col+1]["<"]
    if isinstance(map[row-1][col], dict) and "v" in map[row-1][col] and isinstance(map[row-1][col]["v"], int):
        fromTop = map[row-1][col]["v"]
    if isinstance(map[row+1][col], dict) and "^" in map[row+1][col] and isinstance(map[row+1][col]["^"], int):
        fromBottom = map[row+1][col]["^"]
    
    new = []
    if isinstance(fromLeft, int):
        new.append(fromLeft)
    if isinstance(fromTop, int):
        new.append(fromTop)
    if isinstance(fromBottom, int):
        new.append(fromBottom)
    if isinstance(fromRight, int):
        new.append(fromRight)
    if new != []:
        print(f"result: {min(new)}")
    else:
        print("path not found")

    printMap()

    # and now reverse....
    #
    #
    # ...

    # edit final field
    down = map[endR][endC]["v"]
    up = map[endR][endC]["^"]
    left = map[endR][endC]["<"]
    right = map[endR][endC][">"]

    map[endR][endC]["v"] = min(up, down, left, right)
    map[endR][endC]["^"] = min(up, down, left, right)
    map[endR][endC]["<"] = min(up, down, left, right)
    map[endR][endC][">"] = min(up, down, left, right)

    while True:
        change = False
        for row in range(1, height-1):
            for col in range(1, width-1):
                if map[row][col] == "#":
                    continue
                if row == endR and col == endC:
                    continue                  
                if "v" in map[row][col] and (map[row+1][col] == {} or map[row+1][col] == "#"):
                    map[row][col].pop("v")
                    change = True
                if "^" in map[row][col] and (map[row-1][col] == {} or map[row-1][col] == "#"):
                    map[row][col].pop("^")                    
                    change = True
                if ">" in map[row][col] and (map[row][col+1] == {} or map[row][col+1] == "#"):
                    map[row][col].pop(">")
                    change = True
                if "<" in map[row][col] and (map[row][col-1] == {} or map[row][col-1] == "#"):
                    map[row][col].pop("<")  
                    change = True
                  
                if "v" in map[row][col] and map[row+1][col] != "#":
                    current = map[row][col]["v"]
                    if "v" in map[row+1][col]:
                        down = map[row+1][col]["v"]
                    else:
                        down = 0
                    if "^" in map[row+1][col]:
                        up = map[row+1][col]["^"]
                    else:
                        up = 0
                    if ">" in map[row+1][col]:
                        right = map[row+1][col][">"]
                    else:
                        right = 0
                    if "<" in map[row+1][col]:
                        left = map[row+1][col]["<"]
                    else:
                        left = 0
                    if not (down == current + 1 or left == current + 1001 or right == current + 1001):
                        map[row][col].pop("v")
                        change = True
                if "^" in map[row][col] and map[row-1][col] != "#":
                    current = map[row][col]["^"]
                    if "v" in map[row-1][col]:
                        down = map[row-1][col]["v"]
                    else:
                        down = 0
                    if "^" in map[row-1][col]:
                        up = map[row-1][col]["^"]
                    else:
                        up = 0
                    if ">" in map[row-1][col]:
                        right = map[row-1][col][">"]
                    else:
                        right = 0
                    if "<" in map[row-1][col]:
                        left = map[row-1][col]["<"]
                    else:
                        left = 0
                    if not (left == current + 1001 or right == current + 1001 or up == current + 1):
                        map[row][col].pop("^")
                        change = True
                if ">" in map[row][col] and map[row][col+1] != "#":
                    current = map[row][col][">"]
                    if "v" in map[row][col+1]:
                        down = map[row][col+1]["v"]
                    else:
                        down = 0
                    if "^" in map[row][col+1]:
                        up = map[row][col+1]["^"]
                    else:
                        up = 0
                    if ">" in map[row][col+1]:
                        right = map[row][col+1][">"]
                    else:
                        right = 0
                    if "<" in map[row][col+1]:
                        left = map[row][col+1]["<"]
                    else:
                        left = 0
                    if not (down == current + 1001 or right == current + 1 or up == current + 1001):
                        map[row][col].pop(">")     
                        change = True
                if "<" in map[row][col] and map[row][col-1] != "#":
                    current = map[row][col]["<"]
                    if "v" in map[row][col-1]:
                        down = map[row][col-1]["v"]
                    else:
                        down = 0
                    if "^" in map[row][col-1]:
                        up = map[row][col-1]["^"]
                    else:
                        up = 0
                    if ">" in map[row][col-1]:
                        right = map[row][col-1][">"]
                    else:
                        right = 0
                    if "<" in map[row][col-1]:
                        left = map[row][col-1]["<"]
                    else:
                        left = 0
                    if not (down == current + 1001 or left == current + 1 or up == current + 1001):
                        map[row][col].pop("<")  
                        change = True                                            



        if change == False:
            break
    
    print("reversing finished")
    printMap()
    count = 0
    for row in range(0, height):
        for col in range(0, width):
            if map[row][col] != {} and map[row][col] != "#" :
                count += 1

    print(f"final count: {count=}")                    




if __name__ == "__main__":
    maze()
