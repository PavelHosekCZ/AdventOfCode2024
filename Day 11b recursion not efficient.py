def largeBlinker():
    def blink(current, remaining):
        if remaining == 0:
            return 1
        else:
            if current == "0":
                return blink("1", remaining - 1)
            elif len(current) % 2 == 0:
                return blink(current[: int(len(current)/2)], remaining - 1) \
                    + blink(str(int(current[int(len(current)/2) :])), remaining - 1)
            else:
                return blink(str(int(current) * 2024), remaining - 1)          

    # load data
    input = []
    with open("Day 11 input.txt", 'r') as file:
        input = file.readlines()

    stones = input[0].strip().split(" ") # stones are str

    count = 0
    for stone in stones:
        print(f"{stone=}")
        count += blink(stone, 35)

    print(f"count: {count}")

if __name__ == "__main__":
    largeBlinker()
