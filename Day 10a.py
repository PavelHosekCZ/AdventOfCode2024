def hike():

    def searchAroundForValue(r, c, target):
        if target <= 9:
            value = set()
            if r > 0:
                if map[r-1][c] == target:
                    value = value.union(searchAroundForValue(r-1, c, target+1))
            if r < height - 1:
                if map[r+1][c] == target:
                    value = value.union(searchAroundForValue(r+1, c, target+1))
            if c > 0:
                if map[r][c-1] == target:
                    value = value.union(searchAroundForValue(r, c-1, target+1))
            if c < width - 1:
                if map[r][c+1] == target:
                    value = value.union(searchAroundForValue(r, c+1, target+1))
            return value
        else: 
            if map[r][c] == 9:
                return {tuple([r,c])}
            else:
                return set()

    # load data
    input = []
    with open("Day 10 input.txt", 'r') as file:
        input = file.readlines()

    map = []
    for row in input:
        newRow = []
        for letter in row.strip():
            newRow.append(int(letter))
        map.append(newRow)

    width = len(map[0])
    height = len(map)    


    count = 0

    for row in range(0, height):
        for col in range(0, width):
            if map[row][col] == 0:
                peaks = searchAroundForValue(row, col, 1)
                count += len(peaks)

    print(f"count: {count}")

if __name__ == "__main__":
    hike()
