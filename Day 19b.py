import re

def towelArranging():
   
    # load data
    with open("Day 19 input.txt", 'r') as file:
        dataInput = file.readlines()
        dataLen = len(dataInput)
    
    towels = [towel.strip() for towel in dataInput[0].split(",")]
    print(f"{towels=}")
    print(f"{len(towels)=}")


    count = 0
    valid = 0
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
            #for match in re.finditer(towel, pattern, re.IGNORECASE):
            #    blocks.append([match.start(), match.end() ])
            for j in range(0, patternLen-len(towel)+1):
                if pattern[j:j+len(towel)]== towel:
                    blocks.append([j, j+len(towel)])
        i += 1

        hashmapRaw = {}

        for block in blocks:
            if block[0] in hashmapRaw:
                hashmapRaw[block[0]].append(block[1])
            else:
                hashmapRaw[block[0]] = [block[1]]

        print(f"Raw data:       {hashmapRaw=}")                
        
        hashmap = dict(sorted(hashmapRaw.items()))
        
        print(f"Before optimising: {hashmap=}")

        # remove unused parts of hashmap
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
        # if hashmap became empty after optimalisation, we skip the entire counting part and go directly to the next sequence
        if hashmap == {}:
            continue

        passcounter = {}

        for key, value in hashmap.items():
            newdict = {}
            for item in value:
                newdict[item] = 0
            passcounter[key] = newdict

        # now passcounter contains dicts for counting possible combinations; print to check
        print(f"modified hashmap: {passcounter=}")

        # iterate over every position "j" in flag pattern  
        for j in range(0, patternLen):  
            if j not in passcounter:
                continue  
            # count how many ways lead to this "j" position by counting sum of all towels ending here
            precedingOptions = 0
            if j == 0:
                precedingOptions = 1
            for item in range(0, j+1):
                if item not in passcounter:
                    continue
                endings = passcounter[item]
                for key, value in endings.items():
                    if key == j:
                        precedingOptions += value
            
            #change value of count for each item starting at "j"
            for key in passcounter[j]:
                passcounter[j][key] = precedingOptions

        # now all counters are changed, time to sum up all option counters leading to "patternLen"
        precedingOptions = 0        
        for item in range(0, patternLen):
            if item not in passcounter:
                continue
            endings = passcounter[item]
            for key, value in endings.items():
                if key == patternLen:
                    precedingOptions += value

        print(f"filled hashmap:   {passcounter=}")
        print(f"{precedingOptions=}")   
        count += precedingOptions   
        print(f"{count=}")    
        valid += 1          
    
    print()            
    print(f"Total count: {count}")
    print(f"Valid patterns: {valid}")

if __name__ == "__main__":
    towelArranging()
