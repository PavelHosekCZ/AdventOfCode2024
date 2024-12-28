# Comment: This is the second task where I had to look for help in reddit megathread. I decided to go for a manual solution - visualise
# input data and try to determine which output cables need to be swapped.

def wires():  
    # load data
    with open("Day 24 input.txt", 'r') as file:
        data = file.readlines()

    # skip x, y inputs, not neccessary, extract length of inputs
    i = 0
    while data[i].strip() != "":
        i += 1
    length = int(i/2)

    # save prompts to "prompt" list
    i += 1
    prompts = []
    while i<len(data):
        prompt = {}
        prompt["arg1"] = data[i].split(" ")[0].strip()
        prompt["arg2"] = data[i].split(" ")[2].strip()
        prompt["gate"] = data[i].split(" ")[1].strip()
        prompt["res"] = data[i].split(">")[1].strip()
        prompts.append(prompt)
        i += 1      

    # manually enforced swaps - based on results+ this is the most important part of the code:
    res = []
    # 1
    swap = [175, 142]
    for i, item in enumerate(swap):
        swap[i] = item - (length*2 + 2)
    print(swap)
    prompts[swap[0]]["res"], prompts[swap[1]]["res"] = prompts[swap[1]]["res"], prompts[swap[0]]["res"]
    res.append(prompts[swap[0]]["res"])
    res.append(prompts[swap[1]]["res"])
    
    # 2
    swap = [137, 173]
    for i, item in enumerate(swap):
        swap[i] = item - (length*2 + 2)
    print(swap)
    prompts[swap[0]]["res"], prompts[swap[1]]["res"] = prompts[swap[1]]["res"], prompts[swap[0]]["res"]
    res.append(prompts[swap[0]]["res"])
    res.append(prompts[swap[1]]["res"])    

    # 3
    swap = [155, 275]
    for i, item in enumerate(swap):
        swap[i] = item - (length*2 + 2)
    print(swap)
    prompts[swap[0]]["res"], prompts[swap[1]]["res"] = prompts[swap[1]]["res"], prompts[swap[0]]["res"]  
    res.append(prompts[swap[0]]["res"])
    res.append(prompts[swap[1]]["res"])    

    # 4
    swap = [138, 115]
    for i, item in enumerate(swap):
        swap[i] = item - (length*2 + 2)
    print(swap)
    prompts[swap[0]]["res"], prompts[swap[1]]["res"] = prompts[swap[1]]["res"], prompts[swap[0]]["res"]   
    res.append(prompts[swap[0]]["res"])
    res.append(prompts[swap[1]]["res"])

    # print result
    for item in sorted(res):
        print(f"{item},", end="")



    # swap if "y" is first and "X" second
    for prompt in prompts:
        if prompt["arg1"][1:].isdigit() and prompt["arg2"][1:].isdigit() and prompt["arg1"][0] == "y":
            prompt["arg1"], prompt["arg2"] = prompt["arg2"], prompt["arg1"]
    
    # create list of grouped results with AND prompts
    results = {}
    for prompt in prompts.copy():
        if prompt["arg1"][0] == "x" and prompt["gate"] == "AND":
            num = int(prompt["arg1"][1:3])
            results[num] = [prompt]
            prompts.remove(prompt)
    
    # sort results
    results = dict(sorted(results.items()))

    # add main XOR prompts
    for prompt in prompts.copy():
        if prompt["arg1"][0] == "x":
            num = int(prompt["arg1"][1:3])
            results[num].append(prompt)
            prompts.remove(prompt)

    print(results)

    # add AND and XOR prompts with products of main AND
    temporary = {}
    for key, value in results.items():
        for prompt in value:
            if prompt["gate"] == "XOR":
                temporary[prompt["res"]] = key
    temporary2 = {}
    for key, value in results.items():
        for prompt in value:
            if prompt["gate"] == "AND":
                temporary2[prompt["res"]] = key

    for prompt in prompts.copy():
        if (prompt["arg1"] in temporary or prompt["arg2"] in temporary) and prompt["gate"] == "AND":
            if prompt["arg2"] in temporary:
                prompt["arg1"], prompt["arg2"] = prompt["arg2"], prompt["arg1"]
            num = temporary[prompt["arg1"]]
            results[num].append(prompt)
            prompts.remove(prompt)     
    for prompt in prompts.copy():
        if (prompt["arg1"] in temporary or prompt["arg2"] in temporary) and prompt["gate"] == "XOR":
            if prompt["arg2"] in temporary:
                prompt["arg1"], prompt["arg2"] = prompt["arg2"], prompt["arg1"]
            num = temporary[prompt["arg1"]]
            results[num].append(prompt)
            prompts.remove(prompt)                     

    # add last item
    temporary = temporary2
    for prompt in prompts.copy():
        if (prompt["arg1"] in temporary or prompt["arg2"] in temporary):
            if prompt["arg2"] in temporary:
                prompt["arg1"], prompt["arg2"] = prompt["arg2"], prompt["arg1"]
            num = temporary[prompt["arg1"]]
            results[num].append(prompt)
            prompts.remove(prompt)     




    # print result
    for i,group in results.items():
        print(f"\nnext group {i}:")
        for prompt in group:
            print(f'{prompt["arg1"]} {prompt["gate"]} {prompt["arg2"]} -> {prompt["res"]}')  
    print("\nremaining data:")
    for prompt in prompts:
        print(f'{prompt["arg1"]} {prompt["gate"]} {prompt["arg2"]} -> {prompt["res"]}')  

if __name__ == "__main__":
    wires()
