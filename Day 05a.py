def xmasSearch():
    # load data
    input = []
    with open("Day 05 input.txt", 'r') as file:
        input = file.readlines()
    
    rules = []
    updates = []
    result = 0

    for line in input:
        if "|" in line:
            rules.append(dict([('left', int(line.split('|')[0].strip())), ('right', int(line.split('|')[1].strip()))]))
        if "," in line:
            list_of_integers = [int(x) for x in line.strip().split(",")]
            updates.append(list_of_integers)        

    for update in updates:
        fail = False
        for rule in rules:
            if rule["left"] in update and rule["right"] in update:
                if update.index(rule["left"]) > update.index(rule["right"]):
                    fail = True
        if fail == False:
            result += int(update[int((len(update)-1)/2)])

    print(f"result is: {result}")
            


if __name__ == "__main__":
    xmasSearch()
