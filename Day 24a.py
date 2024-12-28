def wires():  
    # load data
    with open("Day 24 input.txt", 'r') as file:
        data = file.readlines()

    i = 0
    values = {}
    while data[i].strip() != "":
        values[data[i].split(":")[0].strip()] = int(data[i].split(":")[1].strip())
        i += 1

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

    while len(prompts) > 0:
        for i, prompt in enumerate(prompts):
            if prompt["arg1"] not in values or prompt["arg2"] not in values:
                continue
            match prompt["gate"]:
                case "AND":
                    values[prompt["res"]] = values[prompt["arg1"]] and values[prompt["arg2"]]
                case "OR":
                    values[prompt["res"]] = values[prompt["arg1"]] or values[prompt["arg2"]]
                case "XOR":
                    values[prompt["res"]] = values[prompt["arg1"]] ^ values[prompt["arg2"]]
            prompts.pop(i)
            
    print(dict(sorted(values.items())))

    i=0
    resultBinary = ""
    while "z" + str(i).zfill(2) in values:
        resultBinary = str(values["z" + str(i).zfill(2)]) + resultBinary
        i += 1

    print(f"{resultBinary} -> {str(int(resultBinary, 2))}")

if __name__ == "__main__":
    wires()
