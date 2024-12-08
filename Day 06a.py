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
    
    while True:
        match direction:
            case "^":
                if row == 0:
                    break
                if lab[row-1][col] != "#":
                    lab[row-1][col] = "x"
                    row -= 1
                if lab[row-1][col] == "#":
                    direction = ">"
            case "<":
                if col == 0:
                    break
                if lab[row][col-1] != "#":
                    lab[row][col-1] = "x"
                    col -= 1
                if lab[row][col-1] == "#":
                    direction = "^"                
            case ">":
                if col == width - 1:
                    break
                if lab[row][col+1] != "#":
                    lab[row][col+1] = "x"
                    col += 1
                if lab[row][col+1] == "#":
                    direction = "v"                
            case "v":
                if row == height - 1:
                    break      
                if lab[row+1][col] != "#":
                    lab[row+1][col] = "x"
                    row += 1
                if lab[row+1][col] == "#":
                    direction = "<"                     

    count = 0
    for row in lab:
        for col in row:
            if col == "x": 
                count += 1
            print(col, end="")
        print()

    print(f"count: {count}")

if __name__ == "__main__":
    guardTrack()
