def LAN():  
    # load data
    with open("Day 23 input.txt", 'r') as file:
        dataInput = file.readlines()
    connections = [connection.strip() for connection in dataInput]
    connections.sort()
    print(f"{connections=}\n")

    map = {}
    for connection in connections:
        if connection.split("-")[0] in map:
            map[connection.split("-")[0]].append(connection.split("-")[1])
        else: 
            map[connection.split("-")[0]] = [connection.split("-")[1]]
        if connection.split("-")[1] in map:
            map[connection.split("-")[1]].append(connection.split("-")[0])
        else: 
            map[connection.split("-")[1]] = [connection.split("-")[0]]            
    print(f"{map=}\n")
    
    nets = {}
    nets[2] = [connection.strip().split("-") for connection in dataInput]
    n = 3
    while True:
        nets[n] = []
        for base in nets[n-1]:
            for comp in map:
                found = True
                for i in range(0, n-1):
                    if base[i] not in map[comp]:
                        found = False
                if found == True:
                    newNet = base.copy()
                    newNet.append(comp)
                    newNet.sort()
                    if newNet not in nets[n]:
                        nets[n].append(newNet)
        
        print(f"{n=} {len(nets[n])=}")
        if len(nets[n]) == 1:
            break
        n+=1

    print(nets[n][0])
    for item in nets[n][0]:
        print(item + ",", end="")

if __name__ == "__main__":
    LAN()
