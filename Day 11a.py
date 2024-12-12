def blink():
    # load data
    input = []
    with open("Day 11 input.txt", 'r') as file:
        input = file.readlines()

    stones = input[0].strip().split(" ") # stnes are str

    for iteration in range(0, 25): # where the second digit is number of "blinks"
        #print(f"{iteration=}")
        i=0
        while i < len(stones):
            if stones[i] == "0":
                stones[i] = "1"
            elif len(stones[i]) % 2 == 0:
                #print(f"{i=}, {stones[i]=}, {len(stones[i])=}")
                stones.insert(i+1, str(int(stones[i][int(len(stones[i])/2) :])))
                stones[i] = stones[i][: int(len(stones[i])/2)]
                i += 1
            else:
                stones[i] = str(int(stones[i]) * 2024)
            i += 1
        #print(stones)




    count = len(stones)

    print(f"count: {count}")

if __name__ == "__main__":
    blink()
