def LAN():  
    # load data
    with open("Day 23 input.txt", 'r') as file:
        dataInput = file.readlines()
    connections = [connection.strip() for connection in dataInput]
    connections.sort()
    print(f"{connections=}")
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
    print(f"{map=}")
    
    # in each sublist, look for connections of htree computers:
    nets = []
    for first in map:
        for second in map[first]:
            for third in map[second]:
                if third in map[first]:
                    net = [first, second, third]
                    net.sort()
                    if net not in nets:
                        nets.append(net)
    nets.sort()
    print(f"{nets=}")
    print(f"{len(nets)=}")

    # find those with t

    tCount = 0
    for net in nets:
        found = False
        for comp in net:
            if comp[0] == "t":
                found = True
        if found == True:
            tCount += 1
    print(f"{tCount=}")









if __name__ == "__main__":
    LAN()
