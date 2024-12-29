def lock():  
    numPad = {
        "A" : {"row" : 3, "col" : 2},
        "0" : {"row" : 3, "col" : 1},
        "1" : {"row" : 2, "col" : 0},
        "2" : {"row" : 2, "col" : 1},
        "3" : {"row" : 2, "col" : 2},
        "4" : {"row" : 1, "col" : 0},
        "5" : {"row" : 1, "col" : 1},
        "6" : {"row" : 1, "col" : 2},
        "7" : {"row" : 0, "col" : 0},
        "8" : {"row" : 0, "col" : 1},
        "9" : {"row" : 0, "col" : 2}
        }
    arrowPad = {
        "^" : {"row" : 0, "col" : 1},
        "A" : {"row" : 0, "col" : 2},
        "<" : {"row" : 1, "col" : 0},
        "v" : {"row" : 1, "col" : 1},
        ">" : {"row" : 1, "col" : 2}
        }    
        
    def pressNumPad(currentRow, currentCol, target, s):
        if currentRow == numPad[target]["row"] and currentCol == numPad[target]["col"]:
            temp.append(s + "A")
        if currentRow < numPad[target]["row"] and not (currentRow == 2 and currentCol == 0):
            pressNumPad(currentRow + 1, currentCol, target, s + "v")
        if currentRow > numPad[target]["row"]:
            pressNumPad(currentRow - 1, currentCol, target, s + "^")   
        if currentCol < numPad[target]["col"]:
            pressNumPad(currentRow, currentCol + 1, target, s + ">")
        if currentCol > numPad[target]["col"] and not (currentRow == 3 and currentCol == 1):    
            pressNumPad(currentRow, currentCol - 1, target, s + "<")    

    def pressArrowPad(currentRow, currentCol, target, s, temp):
        if currentRow == arrowPad[target]["row"] and currentCol == arrowPad[target]["col"]:
            temp.append(s + "A")
        if currentRow < arrowPad[target]["row"]:
            pressArrowPad(currentRow + 1, currentCol, target, s + "v", temp)
        if currentRow > arrowPad[target]["row"] and not (currentRow == 1 and currentCol == 0):
            pressArrowPad(currentRow - 1, currentCol, target, s + "^", temp)   
        if currentCol < arrowPad[target]["col"]:
            pressArrowPad(currentRow, currentCol + 1, target, s + ">", temp)
        if currentCol > arrowPad[target]["col"] and not (currentRow == 0 and currentCol == 1):
            pressArrowPad(currentRow, currentCol - 1, target, s + "<", temp)

    def findPath(input, lvl):
        if lvl == 0:
            return len(input)
        prev = "A"
        paths = []
        sum = 0
        for item in input:
            temp = []
            pressArrowPad(arrowPad[prev]["row"], arrowPad[prev]["col"], item, "", temp)
            prev = item
            subsum = 10 ** 3
            for subpath in temp:
                res = findPath(subpath, lvl-1)
                if res < subsum:
                    subsum = res
            sum += subsum
            paths.append(temp)
        #print(f"{input=}, {paths=}")            
        return sum

    def combine(lst):
        output = []
        first = lst[0]
        if len(lst) > 1:
            rest = combine(lst[1:])
        else:
            temp = []
            for i in lst[0]:
                temp.append([i])
            return temp
        for i in first:
            for j in rest:
                output.append([i] + j)
        return output


    # load data
    with open("Day 21 input.txt", 'r') as file:
        data = file.readlines()
    
    # push buttons for each line of input
    result = 0
    for line in data:
        prompt = line.strip()
        prev = "A"
        paths = []
        for letter in prompt:
            temp = []
            pressNumPad(numPad[prev]["row"], numPad[prev]["col"], letter, "")
            prev = letter
            paths.append(temp)

        #print(f"{paths=}") # example: paths=[['<A'], ['^A'], ['^^>A', '^>^A', '>^^A'], ['vvvA']]

        combinedPathsLists = combine(paths)

        #print(f"{combinedPathsLists=}") # example: combinedPathsLists=[['<A', '^A', '^^>A', 'vvvA'], ['<A', '^A', '^>^A', 'vvvA'], ['<A', '^A', '>^^A', 'vvvA']]

        inputs = []
        for lst in combinedPathsLists:
            temp = ""
            for item in lst:
                temp = temp + item
            inputs.append(temp)

        #print(f"{inputs=}")    
        #print()    

        # example: inputs=['<A^A^^>AvvvA', '<A^A^>^AvvvA', '<A^A>^^AvvvA']

        presses = 10 ** 3
        for input in inputs:
            num = findPath(input, 2)
            if num < presses:
                presses = num
            #print(f"{input} -> {num}")
        
        combo = presses * int(prompt[:-1])
        result += combo
        print(f"{prompt=}, {presses=}, {combo=}")
    print(f"{result=}")











if __name__ == "__main__":
    lock()
