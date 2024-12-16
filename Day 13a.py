def claw():
    # load data
    input = []
    with open("Day 13 input.txt", 'r') as file:
        input = file.readlines()
    
    i=0
    count = 0
    while i < len(input):
        Xa = int(input[i].strip().split("+")[1].split(",")[0])
        Ya = int(input[i].strip().split("+")[2])
        i+=1
        Xb = int(input[i].strip().split("+")[1].split(",")[0])
        Yb = int(input[i].strip().split("+")[2])
        i+=1
        Xtarget = int(input[i].strip().split("=")[1].split(",")[0])
        Ytarget = int(input[i].strip().split("=")[2]) 
        i+=2
        print(f"{Xa=}, {Ya=}, {Xb=}, {Yb=}, {Xtarget=}, {Ytarget=}")        

        denominator = Ya * Xb - Xa * Yb
        if denominator == 0:
            print("vectors parallel")
            continue
        v = (Ya * Xtarget - Xa * Ytarget) / denominator
        u = (Xtarget - v * Xb) / Xa

        X = Xa * round(u) + Xb * round(v)
        Y = Ya * round(u) + Yb * round(v)
        
        if X == Xtarget and Y == Ytarget and 0 <= u <= 100 and 0 <= v <= 100:
            count += round(u) * 3 + round(v) * 1



    print(f"count: {count}")

if __name__ == "__main__":
    claw()
