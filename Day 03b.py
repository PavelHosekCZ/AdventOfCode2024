def multiply():
    # load data
    lines = []
    with open("Day 03 input.txt", 'r') as file:
        lines = file.readlines()

    multiplications = 0

    enabled = True

    for line in lines:
        print("\nLINE: " + line)
        line = "x" + line # this ensures that first part in parts is never the beginning of "mul("
        subline = ""
        parts = line.split("mul(")
        skipFirst = True
        for part in parts:
            print("PART: " + part)
            if skipFirst:
                subline = subline + " " * len(part)
                skipFirst = False
                print("SKIP")
                continue
            subparts = part.split(",", 1)
            if len(subparts) >= 2:
                firstNumber = subparts[0]
                rest = subparts[1]
                secondNumber = rest.split(")")[0]
                print("  [ " + firstNumber + " " + secondNumber + " ]")

                if firstNumber.isdigit() and secondNumber.isdigit() and enabled:
                    multiplications += int(firstNumber) * int(secondNumber)
                    print("  > " + str(int(firstNumber) * int(secondNumber)) + "       ..." + str(multiplications))
                    subline = subline + "MUL(" + firstNumber + "," + secondNumber + ")" + " " * (len(part) - 2 - len(firstNumber) - len(secondNumber))
                else:
                    subline = subline + "XXX(" + " " * len(part)
            else:
                subline = subline + "XXX(" + " " * len(part)                    

            if "do()" in part:
                enabled = True
            if "don't()" in part:
                enabled = False

        
        print("rekapitulace:")
        print(line)
        print(subline)

    print("final count: " + str(multiplications))


if __name__ == "__main__":
    multiply()
