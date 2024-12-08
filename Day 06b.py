import copy

def guardTrack():
    # load data
    input = []
    with open("Day 06 input.txt", 'r') as file:
        input = file.readlines()
    lab = []
    for row in input:
        newRow = []
        for letter in row.strip():
            newRow.append(letter)
        lab.append(newRow)

    width = len(lab[0])
    height = len(lab)

    for row in range(0, height):
        for col in range(0, width):
            if lab[row][col] == "^":
                pos_col = col
                pos_row = row
                direction = "^"
                lab[row][col] = "x"
                break

    col = pos_col
    row = pos_row

    emptyLab = copy.deepcopy(lab) # saving original lab for later

    # first run - marking all visited positions by "x" for later
    while True:
        match direction:
            case "^":
                if row == 0:
                    break
                if lab[row-1][col] != "#":
                    lab[row-1][col] = "x"
                    row -= 1
                else:
                    direction = ">"
            case "<":
                if col == 0:
                    break
                if lab[row][col-1] != "#":
                    lab[row][col-1] = "x"
                    col -= 1
                else:
                    direction = "^"                
            case ">":
                if col == width - 1:
                    break
                if lab[row][col+1] != "#":
                    lab[row][col+1] = "x"
                    col += 1
                else:
                    direction = "v"                
            case "v":
                if row == height - 1:
                    break      
                if lab[row+1][col] != "#":
                    lab[row+1][col] = "x"
                    row += 1
                else:
                    direction = "<"      

    # with unaltered trajectory marked in lab, get a list of all possible obstacles: 
    obstacles = []
    for row in range(0, height):
        for col in range(0, width):
            if lab[row][col] == "x": 
                obstacles.append({"row": row, "col": col})
    obstacles.remove({"row": pos_row, "col": pos_col})
    
    # now run all again for all possible obstacle locations
    count = 0
    i = 0
    for obstacle in obstacles:
        print()
        print(f"Obstacle {i} of {len(obstacles)}")
        i += 1
        col = pos_col
        row = pos_row
        direction = "^"   
        lab = copy.deepcopy(emptyLab)       
        lab[obstacle["row"]][obstacle["col"]] = "#"
        hit = []
        loop = False
        while True:
            match direction:
                case "^":
                    if row == 0:
                        break
                    if lab[row-1][col] != "#":
                        lab[row-1][col] = "x"
                        row -= 1
                    else:
                        direction = ">"
                        if f"R{row-1}C{col}^" in hit:
                            loop = True
                            break
                        else:
                            hit.append(f"R{row-1}C{col}^")
                case "<":
                    if col == 0:
                        break
                    if lab[row][col-1] != "#":
                        lab[row][col-1] = "x"
                        col -= 1
                    else:
                        direction = "^"   
                        if f"R{row}C{col-1}<" in hit:
                            loop = True
                            break
                        else:
                            hit.append(f"R{row}C{col-1}<")                                     
                case ">":
                    if col == width - 1:
                        break
                    if lab[row][col+1] != "#":
                        lab[row][col+1] = "x"
                        col += 1
                    else:
                        direction = "v"       
                        if f"R{row}C{col+1}>" in hit:
                            loop = True
                            break
                        else:
                            hit.append(f"R{row}C{col+1}>")                                 
                case "v":
                    if row == height - 1:
                        break      
                    if lab[row+1][col] != "#":
                        lab[row+1][col] = "x"
                        row += 1
                    else:
                        direction = "<"   
                        if f"R{row+1}C{col}v" in hit:
                            loop = True
                            break
                        else:
                            hit.append(f"R{row+1}C{col}v")                        
        if loop == True:
            count += 1
            print("LOOP")
        else:
            print("no loop")


    print(f"count: {count}")

if __name__ == "__main__":
    guardTrack()
