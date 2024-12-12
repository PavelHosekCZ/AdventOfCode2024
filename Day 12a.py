def buildPlots():
    def search(r, c, letter):
        # I am always on a valid unsearched field. Marking current field, setting default area and perimeter value
        mapped[r][c] = "x"
        a = 1
        p = 0

        # searching surrounding fields in four directions
        if r > 0:
            if map[r-1][c] == letter and mapped[r-1][c] == ".":
                aa, pp = search(r-1, c, letter)
                a += aa
                p += pp
            elif map[r-1][c] != letter:
                p += 1
        else:
            p += 1

        if c > 0:
            if map[r][c-1] == letter and mapped[r][c-1] == ".":
                aa, pp = search(r, c-1, letter)
                a += aa
                p += pp
            elif map[r][c-1] != letter:
                p += 1
        else:
            p += 1

        if r < height - 1:
            if map[r+1][c] == letter and mapped[r+1][c] == ".":
                aa, pp = search(r+1, c, letter)
                a += aa
                p += pp
            elif map[r+1][c] != letter:
                p += 1
        else:
            p += 1

        if c < width - 1:
            if map[r][c+1] == letter and mapped[r][c+1] == ".":
                aa, pp = search(r, c+1, letter)
                a += aa
                p += pp
            elif map[r][c+1] != letter:
                p += 1
        else:
            p += 1            

        # returning area (a) and perimeter (p)
        return a, p


    # load data
    input = []
    with open("Day 12 input.txt", 'r') as file:
        input = file.readlines()

    map = [row.strip() for row in input]

    width = len(map[0])
    height = len(map)    

    mapped = [["." for j in range(0, width)] for i in range(0, height)]


    count = 0

    for row in range(0, height):
        for col in range(0, width):
            if mapped[row][col] == ".":
                area, perimeter = search(row, col, map[row][col])
                count += area * perimeter

    print(f"count: {count}")

if __name__ == "__main__":
    buildPlots()
