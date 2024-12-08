def xmasSearch():
    # load data
    table = []
    with open("Day 04 input.txt", 'r') as file:
        table = file.readlines()
    width = len(table[0])-1 # assuming table has at least one row; last char is ommited because it is end of line
    height = len(table)
    word = "MAS"
    count = 0

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if table[row][col] == "A":
                #diagonally to up left
                if (
                    ((table[row-1][col-1] == "M" and table[row+1][col+1] == "S") or (table[row-1][col-1] == "S" and table[row+1][col+1] == "M")) and 
                    ((table[row+1][col-1] == "M" and table[row-1][col+1] == "S") or (table[row+1][col-1] == "S" and table[row-1][col+1] == "M"))
                ):
                    count += 1                

                                                        

    print(f"final count: {count}")


if __name__ == "__main__":
    xmasSearch()
