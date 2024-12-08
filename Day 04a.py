def xmasSearch():
    # load data
    table = []
    with open("Day 04 input.txt", 'r') as file:
        table = file.readlines()
    width = len(table[0])-1 # assuming table has at least one row; last char is ommited because it is end of line
    height = len(table)
    word = "XMAS"
    count = 0

    for row in range(0, height):
        for col in range(0, width):
            if table[row][col] == "X":
                #left to right
                if col <= width - len(word):
                    if table[row][col+1] == "M" and table[row][col+2] == "A" and table[row][col+3] == "S":
                        count += 1
                #right to left
                if col >= len(word) - 1:
                    if table[row][col-1] == "M" and table[row][col-2] == "A" and table[row][col-3] == "S":
                        count += 1      
                #top to bottom
                if row <= height - len(word):
                    if table[row+1][col] == "M" and table[row+2][col] == "A" and table[row+3][col] == "S":
                        count += 1
                #bottom to top
                if row >= len(word) - 1:
                    if table[row-1][col] == "M" and table[row-2][col] == "A" and table[row-3][col] == "S":
                        count += 1        
                #diagonally to up left
                if col >= len(word) - 1 and row >= len(word) - 1:
                    if table[row-1][col-1] == "M" and table[row-2][col-2] == "A" and table[row-3][col-3] == "S":
                        count += 1                
                #diagonally to up right
                if col <= width - len(word) and row >= len(word) - 1:
                    if table[row-1][col+1] == "M" and table[row-2][col+2] == "A" and table[row-3][col+3] == "S":
                        count += 1    
                #diagonally to down left
                if col >= len(word) - 1 and row <= height - len(word):
                    if table[row+1][col-1] == "M" and table[row+2][col-2] == "A" and table[row+3][col-3] == "S":
                        count += 1
                #diagonally to down right  
                if col <= width - len(word) and row <= height - len(word):
                    if table[row+1][col+1] == "M" and table[row+2][col+2] == "A" and table[row+3][col+3] == "S":
                        count += 1
               
                                                        

    print(f"final count: {count}")


if __name__ == "__main__":
    xmasSearch()
