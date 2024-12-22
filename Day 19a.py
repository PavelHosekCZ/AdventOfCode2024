import re

def towelArranging():
    # load data
    with open("Day 19 input.txt", 'r') as file:
        dataInput = file.readlines()
        dataLen = len(dataInput)
    
    towels = [towel.strip() for towel in dataInput[0].split(",")]
    print(f"{towels=}")

    count = 0
    i = 2
    while i < dataLen:
        pattern = dataInput[i].strip()
        print(pattern)
        print(f"{len(pattern)=}")
        blocks = []
        for towel in towels:
            for match in re.finditer(towel, pattern, re.IGNORECASE):
                blocks.append([match.start(), match.end() ])
        i += 1
        print(blocks)
        print(f"{len(blocks)=}")

        next = [0]
        while len(next) > 0:
            current = min(next)
            next.remove(current)
            for block in blocks:
                if block[0] == current:
                    if block[1] not in next:
                        next.append(block[1])


        
        if current == len(pattern):
            print("FOUND")
            count += 1
        else:
            print("NOT found")
        
    print(f"count: {count}")

if __name__ == "__main__":
    towelArranging()
