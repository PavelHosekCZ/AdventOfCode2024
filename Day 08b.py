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
                deltar = ant2r - ant1r
                deltac = ant2c - ant1c
                node_r = ant1r
                node_c = ant1c
                while (node_r >= 0 and node_r < height) and (node_c >= 0 and node_c < width):
                    target[node_r][node_c] = "#"
                    node_r += deltar
                    node_c += deltac
                node_r = ant1r
                node_c = ant1c
                while (node_r >= 0 and node_r < height) and (node_c >= 0 and node_c < width):
                    target[node_r][node_c] = "#"
                    node_r -= deltar
                    node_c -= deltac


    for row in target:
        for col in row:
            if col == "#": 
                count += 1
            print(col, end="")
        print()


    print(f"count: {count}")



if __name__ == "__main__":
    overlaps()
