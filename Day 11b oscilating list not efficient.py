def largeBlinker():
    # load data
    input = []
    with open("Day 11 input.txt", 'r') as file:
        input = file.readlines()

    stones = input[0].strip().split(" ") # stones are str

    count = 0
    repetitions = 75

    # handling input values one by one
    for stone in stones: 
        tasks = []
        tasks.append({"v": stone, "r": 0})

        while len(tasks) > 0:
            task = tasks.pop()
            v = task["v"]
            r = task["r"]
            while r < repetitions:
                if v == "0":
                    v = "1"
                elif len(v) % 2 == 0:
                    tasks.append({"v": str(int(v[int(len(v)/2) :])), "r": r+1})
                    v = v[: int(len(v)/2)]                    
                else:
                    v = str(int(v) * 2024)    
                r += 1
            count += 1


    print(f"count: {count}")

if __name__ == "__main__":
    largeBlinker()
