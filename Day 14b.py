def predict():
    # load data
    input = []
    with open("Day 14 input.txt", 'r') as file:
        input = file.readlines()

    width = 101
    height = 103
    time =5000
    robots = len(input)
    
    # solution is higher than 5 000 and lower than 50 000; very close at 49 892; this was found out by trial and error...
    while time < 50000:
        map = []    
        neighbourIndex = 0

        for row in range(0,height):
            map.append(["."] * width)

        for robot in input:
            x = int(robot.split("=")[1].split(",")[0].strip())
            y = int(robot.split("=")[1].split(",")[1].split(" ")[0].strip())
            u = int(robot.split("=")[2].split(",")[0].strip())
            v = int(robot.split("=")[2].split(",")[1].strip())
            
            xx = (x + time * u) % width
            yy = (y + time * v) % height

            if map[yy][xx] == ".":
                map[yy][xx] = 1
            else: 
                map[yy][xx] += 1 

        # checking for neighbours - expecting that the image is made of several robots immediately next to each other
        for x in range(0, width):
            for y in range(0, height):
                if isinstance(map[y][x], int):
                    neighbours = False
                    if x > 0:
                        if isinstance(map[y][x-1], int):
                            neighbours = True
                    if y > 0:
                        if isinstance(map[y-1][x], int):
                            neighbours = True
                    if x < width - 1:
                        if isinstance(map[y][x+1], int):
                            neighbours = True
                    if y < height - 1:
                        if isinstance(map[y+1][x], int):
                            neighbours = True
                    if neighbours == True:
                        neighbourIndex += 1

        if neighbourIndex / robots > 0.5:               
            print(f"current time: {time}")
            for x in range(0, width):
                for y in range(0, height):
                    print(map[y][x], end="")
                print()
            print()
            print()
            print()
            print()                

        time += 1

        


if __name__ == "__main__":
    predict()
