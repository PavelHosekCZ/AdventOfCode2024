def predict():
    # load data
    input = []
    with open("Day 14 input.txt", 'r') as file:
        input = file.readlines()

    width = 101
    height = 103
    #width = 11
    #height = 7
    time = 100
    
    map_start = []
    map_end = []    
    count = 1

    for row in range(0,height):
        map_start.append(["."] * width)
    for row in range(0,height):
        map_end.append(["."] * width)

    for robot in input:
        x = int(robot.split("=")[1].split(",")[0].strip())
        y = int(robot.split("=")[1].split(",")[1].split(" ")[0].strip())
        u = int(robot.split("=")[2].split(",")[0].strip())
        v = int(robot.split("=")[2].split(",")[1].strip())

        if map_start[y][x] == ".":
            map_start[y][x] = 1
        else: 
            map_start[y][x] += 1 
        
        xx = (x + time * u) % width
        yy = (y + time * v) % height

        if map_end[yy][xx] == ".":
            map_end[yy][xx] = 1
        else: 
            map_end[yy][xx] += 1 
    
    count_part = 0
    for x in range(0, int(width/2-0.5)):
        for y in range(0, int(height/2-0.5)):
            if isinstance(map_end[y][x], int): 
                count_part += map_end[y][x]
    count *= count_part

    count_part = 0
    for x in range(int(width/2+0.5), width):
        for y in range(0, int(height/2-0.5)):
            if isinstance(map_end[y][x], int):                 
                count_part += map_end[y][x]
    count *= count_part 

    count_part = 0
    for x in range(0, int(width/2-0.5)):
        for y in range(int(height/2+0.5), height):
            if isinstance(map_end[y][x], int):                 
                count_part += map_end[y][x]
    count *= count_part 

    count_part = 0
    for x in range(int(width/2+0.5), width):
        for y in range(int(height/2+0.5), height):
            if isinstance(map_end[y][x], int):                 
                count_part += map_end[y][x]
    count *= count_part

    print(f"count: {count}")

if __name__ == "__main__":
    predict()
