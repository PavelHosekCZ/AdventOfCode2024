# Comment:
# This one was hard and I needed some inspiration from other solvers. 
# Solution is designed specifically for my input - it might not work for someone else's.
# My initial sequence was such that prompt "bst" eventually initialised all registers A, B and C. 
# It also meant that each element of the output is effected by different part of input value (8 to the power numbers in range 0 to 15).

def computer():  
    def valueA():
        A = 0
        for i in range(0,16):
            A += indexes[i] * 8**i
        return A
    
    def render(level):
        for j in range(0,8):
            if level == 15 and j == 0:
                continue
            indexes[level] = j
            res = calculate(valueA())
            if res[level] == program[level]:
                if level > 0:
                    render(level-1)
                else: 
                    print(f"Result found: {valueA()}")
    
    def calculate(regA):
        regB = int(data[1].split(":")[1].strip())
        regC = int(data[2].split(":")[1].strip())        
        i = 0
        output = []

        while i < len(program):
            match program[i]:
                case 0: #adv
                    if program[i+1] <= 3: denom = 2**program[i+1]
                    elif program[i+1] == 4: denom = 2**regA
                    elif program[i+1] == 5: denom = 2**regB
                    elif program[i+1] == 6: denom = 2**regC
                    else: return []
                    regA = int(regA / denom)
                case 1: #bxl
                    regB = program[i+1] ^ regB
                case 2: #bst
                    if program[i+1] <= 3: combo = program[i+1]
                    elif program[i+1] == 4: combo = regA
                    elif program[i+1] == 5: combo = regB
                    elif program[i+1] == 6: combo = regC
                    else: return []
                    regB = combo % 8
                case 3: #jnz
                    if regA != 0:
                        i = program[i+1] - 2
                case 4: #bxc
                    regB = regB ^ regC
                case 5: #out
                    if program[i+1] <= 3: combo = program[i+1]
                    elif program[i+1] == 4: combo = regA
                    elif program[i+1] == 5: combo = regB
                    elif program[i+1] == 6: combo = regC
                    else: return []
                    newnum = combo % 8
                    output.append(newnum)
                case 6: #bdv
                    if program[i+1] <= 3: denom = 2**program[i+1]
                    elif program[i+1] == 4: denom = 2**regA
                    elif program[i+1] == 5: denom = 2**regB
                    elif program[i+1] == 6: denom = 2**regC
                    else: return []
                    regB = int(regA / denom)
                case 7: #cdv
                    if program[i+1] <= 3: denom = 2**program[i+1]
                    elif program[i+1] == 4: denom = 2**regA
                    elif program[i+1] == 5: denom = 2**regB
                    elif program[i+1] == 6: denom = 2**regC
                    else: return []                    
                    regC = int(regA / denom)
            i += 2   
        return(output)
    
    # load data
    with open("Day 17 input.txt", 'r') as file:
        data = file.readlines()
    program = [int(prog.strip()) for prog in data[4].split(":")[1].split(",")]

    indexes = {}
    for i in range(0,16):
        indexes[i] = 0

    render(15)

    


    


if __name__ == "__main__":
    computer()

