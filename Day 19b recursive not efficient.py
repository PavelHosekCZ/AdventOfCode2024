import re

def towelArranging():
    def reachFlag(num):
        if num == patternLen:
            l = optionCounter[0]
            optionCounter[0] = l + 1
            if optionCounter[0] % 1000000 == 0:
                print(optionCounter[0]) 
            return
        for item in hashmap[num]:
            reachFlag(item)
   
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
        print()
        print("NEXT PATTERN: ")
        print(pattern)
        patternLen = len(pattern)
        print(f"{patternLen=}")
        blocks = []
        for towel in towels:
            for match in re.finditer(towel, pattern, re.IGNORECASE):
                blocks.append([match.start(), match.end() ])
        i += 1

        hashmap = {}

        for block in blocks:
            if block[0] in hashmap:
                hashmap[block[0]].append(block[1])
            else:
                hashmap[block[0]] = [block[1]]
        
        hashmap = dict(sorted(hashmap.items()))
        
        print(f"Before optimising: {hashmap=}")

        while True:
            changed = False
            for j in range(0, patternLen):
                # if no block starts at field "j", it is neccesary to delete all blocks that end at "j" as they are dead ends.
                if j not in hashmap:
                    # delete all blocks ending at "j"
                    for item in hashmap.values():
                        if j in item: 
                            item.remove(j)
                            changed = True

                # if no block ends at field "j", it is neccesary to delete all blocks that start at "j" as they can not be reached from start.
                found = False
                for item in hashmap.values():
                    if j in item: 
                        found = True
                if found == False and j > 0:
                    if j in hashmap.keys():
                        hashmap.pop(j)
                        changed = True

                # remove empty items of dictionary
                if j in hashmap and hashmap[j] == []:
                    hashmap.pop(j)
                    changed = True
                        
            if changed == False:
                break

        print(f"After optimising:  {hashmap=}")

        # now counting possible ways to make the flag
        optionCounter = [0]
        if hashmap != {}:
            reachFlag(0)
        count += optionCounter[0]
        print(f"number of options: {optionCounter[0]=}")
        print(f"{count=}")   
                    
    print(f"count: {count}")

if __name__ == "__main__":
    towelArranging()
