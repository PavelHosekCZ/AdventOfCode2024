def blink():
    # load data
    input = []
    with open("Day 11 input.txt", 'r') as file:
        input = file.readlines()

    stones =  {stone: 1 for stone in input[0].strip().split(" ")} # stones are str

    print(f"{stones=}")
 
    for iteration in range(0, 75): # where the second digit is number of "blinks"
        print(f"{iteration=}")
        new = {}
        for key, value in stones.items():
            if key == "0":
                if "1" in new:
                    new["1"] += value
                else:
                    new["1"] = value
            elif len(key) % 2 == 0:
                if str(int(key[int(len(key)/2) :])) in new:
                    new[str(int(key[int(len(key)/2) :]))] += value
                else:
                    new[str(int(key[int(len(key)/2) :]))] = value
                if key[: int(len(key)/2)] in new:
                    new[key[: int(len(key)/2)]] += value            
                else:
                    new[key[: int(len(key)/2)]] = value            
            else:
                if str(int(key) * 2024) in new:
                    new[str(int(key) * 2024)] += value
                else:
                    new[str(int(key) * 2024)] = value

        stones = new
        print(stones)

    count = 0
    for value in stones.values():
        count += int(value)

    print(f"count: {count}")

if __name__ == "__main__":
    blink()
