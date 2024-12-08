def calculate(finalProduct: int, prevProduct: int, remainingList: list):
    if remainingList:
        if (
            calculate(finalProduct, prevProduct * remainingList[0], remainingList[1:])
            or calculate(finalProduct, prevProduct + remainingList[0], remainingList[1:])
        ):
            return True
        else:
            return False
    else:
        if finalProduct == prevProduct:
            return True
        else:
            return False


def calibration():
    # load data
    input = []
    with open("Day 07 input.txt", 'r') as file:
        input = file.readlines()

    count = 0

    for line in input:
        res, num = line.split(":")
        result = int(res.strip())
        numbers = num.strip().split(" ")
        numbers = [int(x.strip()) for x in numbers]

        if calculate(result, 0, numbers): 
            count += result

    print(f"count: {count}")

if __name__ == "__main__":
    calibration()
