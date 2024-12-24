import math

def market():  
    # load data
    with open("Day 22 input.txt", 'r') as file:
        dataInput = file.readlines()
    sum = 0
    for number in dataInput:
        num = int(number.strip())
        for i in range(0, 2000):
            # step 1
            res = num * 64
            num = res ^ num
            num = num % 16777216

            # step 2
            res = math.floor(num / 32)
            num = res ^ num
            num = num % 16777216

            # step 3    
            res = num * 2048
            num = res ^ num
            num = num % 16777216
        print(f"After 2000 repetitions, number {number.strip()} became {num}")
        sum += num
    print(f"Final sum is {sum}.")




if __name__ == "__main__":
    market()
