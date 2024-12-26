def computer():  
    # load data
    with open("Day 17 input.txt", 'r') as file:
        data = file.readlines()
    regA = int(data[0].split(":")[1].strip())
    regB = int(data[1].split(":")[1].strip())
    regC = int(data[2].split(":")[1].strip())
    program = [int(prog.strip()) for prog in data[4].split(":")[1].split(",")]

    #print(f"{regA=}, {regB=}, {regC=}, {program=}") #input data processed correctly
    i = 0
    while i < len(program):
        match program[i]:
            case 0: #adv
                if program[i+1] <= 3: denom = 2**program[i+1]
                if program[i+1] == 4: denom = 2**regA
                if program[i+1] == 5: denom = 2**regB
                if program[i+1] == 6: denom = 2**regC
                regA = int(regA / denom)
            case 1: #bxl
                regB = program[i+1] ^ regB
            case 2: #bst
                if program[i+1] <= 3: combo = program[i+1]
                if program[i+1] == 4: combo = regA
                if program[i+1] == 5: combo = regB
                if program[i+1] == 6: combo = regC
                regB = combo % 8
            case 3: #jnz
                if regA != 0:
                    i = program[i+1] - 2
            case 4: #bxc
                regB = regB ^ regC
            case 5: #out
                if program[i+1] <= 3: combo = program[i+1]
                if program[i+1] == 4: combo = regA
                if program[i+1] == 5: combo = regB
                if program[i+1] == 6: combo = regC
                print(combo % 8, end=",")
            case 6: #bdv
                if program[i+1] <= 3: denom = 2**program[i+1]
                if program[i+1] == 4: denom = 2**regA
                if program[i+1] == 5: denom = 2**regB
                if program[i+1] == 6: denom = 2**regC
                regB = int(regA / denom)
            case 7: #cdv
                if program[i+1] <= 3: denom = 2**program[i+1]
                if program[i+1] == 4: denom = 2**regA
                if program[i+1] == 5: denom = 2**regB
                if program[i+1] == 6: denom = 2**regC
                regC = int(regA / denom)
        i += 2        

    print(f"\nProgram terminated. Reg values: {regA=}, {regB=}, {regC=}")


if __name__ == "__main__":
    computer()

