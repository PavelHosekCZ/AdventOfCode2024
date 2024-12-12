def buildPlots():
    def search(r, c, letter):
        # I am always on a valid unsearched field. Marking current field, setting default area, perimeter and corners value
        mapped[r][c] = "x"
        a = 1
        p = 0
        n = 0
        sur00 = "."  
        sur01 = "."  
        sur02 = "."  
        sur10 = "."  
        sur12 = "."  
        sur20 = "."  
        sur21 = "."  
        sur22 = "."  
 

        # searching surrounding fields in four directions
        if r > 0:
            if map[r-1][c] == letter and mapped[r-1][c] == ".":
                aa, pp, nn = search(r-1, c, letter)
                a += aa
                p += pp
                n += nn
                sur01 = "1"
            elif map[r-1][c] != letter:
                p += 1
                sur01 = "0"
            else:
                sur01 = "1"
        else:
            p += 1
            sur01 = "0"

        if c > 0:
            if map[r][c-1] == letter and mapped[r][c-1] == ".":
                aa, pp, nn = search(r, c-1, letter)
                a += aa
                p += pp
                n += nn
                sur10 = "1"
            elif map[r][c-1] != letter:
                p += 1
                sur10 = "0"
            else:
                sur10 = "1"
        else:
            p += 1
            sur10 = "0"

        if r < height - 1:
            if map[r+1][c] == letter and mapped[r+1][c] == ".":
                aa, pp, nn = search(r+1, c, letter)
                a += aa
                p += pp
                n += nn
                sur21 = "1"
            elif map[r+1][c] != letter:
                p += 1
                sur21 = "0"
            else:
                sur21 = "1"
        else:
            p += 1
            sur21 = "0"

        if c < width - 1:
            if map[r][c+1] == letter and mapped[r][c+1] == ".":
                aa, pp, nn = search(r, c+1, letter)
                a += aa
                p += pp
                n += nn
                sur12 = "1"
            elif map[r][c+1] != letter:
                p += 1
                sur12 = "0"
            else:
                sur12 = "1"
        else:
            p += 1    
            sur12 = "0"     

        # mapping surrounding
        if r > 0 and c > 0:
            if map[r-1][c-1] == letter:
                sur00 = "1"
            else:
                sur00 = "0"
        else: sur00 = "0"

        if r > 0 and c < width - 1:
            if map[r-1][c+1] == letter:
                sur02 = "1"
            else:
                sur02 = "0"
        else: sur02 = "0"       

        if r < height - 1 and c > 0:
            if map[r+1][c-1] == letter:
                sur20 = "1"
            else:
                sur20 = "0"
        else: sur20 = "0"

        if r < height - 1 and c < width - 1:
            if map[r+1][c+1] == letter:
                sur22 = "1"
            else:
                sur22 = "0"
        else: sur22 = "0"       


        # counting corners
        if sur01 == "0" and sur12 == "0" : # ^>  inside corner
            n += 1
        if sur12 == "0" and sur21 == "0" : # >v  inside corner
            n += 1
        if sur21 == "0" and sur10 == "0" : # v<  inside corner
            n += 1
        if sur10 == "0" and sur01 == "0" : # <^  inside corner
            n += 1

        if sur01 == "1" and sur12 == "1" and sur02 == "0" : # ^> 
            n += 1  
        if sur12 == "1" and sur21 == "1" and sur22 == "0" : # >v 
            n += 1  
        if sur21 == "1" and sur10 == "1" and sur20 == "0" : # v< 
            n += 1   
        if sur10 == "1" and sur01 == "1" and sur00 == "0" : # <^ 
            n += 1



        # returning area (a), perimeter (p), corners (c)
        return a, p, n


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
                area, perimeter, corners = search(row, col, map[row][col])
                count += area * corners

    print(f"count: {count}")

if __name__ == "__main__":
    buildPlots()
