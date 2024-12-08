def overlaps():
    # load data
    input = []
    with open("Day 08 input.txt", 'r') as file:
        input = file.readlines()
    
    map = []
    target = []
    for row in input:
        newRow = []
        targetRow = []
        for letter in row.strip():
            newRow.append(letter)
            targetRow.append(".")
        map.append(newRow)
        target.append(targetRow)

    width = len(map[0])
    height = len(map)    

    count = 0

    symbols = dict()

    for row in range(0, height):
        for col in range(0, width):
            if map[row][col] != ".":
                if map[row][col] in symbols:
                    symbols[map[row][col]].append({"row": row, "col": col})
                else: 
                    symbols[map[row][col]] = [{"row": row, "col": col}]

    print(symbols)

    for symbol in symbols.keys():
        print(symbol)
        print(symbols[symbol])
        print("a teď co s tím")
        for i in range(0, len(symbols[symbol])):
            for j in range(i+1, len(symbols[symbol])):
                ant1r = symbols[symbol][i]["row"]
                ant1c = symbols[symbol][i]["col"]
                ant2r = symbols[symbol][j]["row"]
                ant2c = symbols[symbol][j]["col"]
                node1r = ant1r - (ant2r - ant1r)
                node1c = ant1c - (ant2c - ant1c)
                node2r = ant2r - (ant1r - ant2r)
                node2c = ant2c - (ant1c - ant2c)
                if (node1r >= 0 and node1r < height) and (node1c >= 0 and node1c < width):
                    target[node1r][node1c] = "#"
                if (node2r >= 0 and node2r < height) and (node2c >= 0 and node2c < width):
                    target[node2r][node2c] = "#"

    for row in target:
        for col in row:
            if col == "#": 
                count += 1
            print(col, end="")
        print()


    print(f"count: {count}")



if __name__ == "__main__":
    overlaps()
