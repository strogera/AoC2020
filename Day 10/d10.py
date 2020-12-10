from collections import defaultdict

def partOne():
    with open("input.txt", "r") as inputFile:
        data=[int(x) for x in inputFile.readlines()]
        data=sorted(data)
        diff1jolt=0
        diff3jolt=0
        outlet=0
        for jolt in data:
            diff=jolt-outlet
            if diff == 1:
                diff1jolt+=1
            elif diff == 3:
                diff3jolt+=1
            outlet=jolt
        return diff1jolt*(diff3jolt+1)

def makeGraph(data):
    data.append(data[-1]+3)
    data=[0]+data
    graph=defaultdict(list)
    graph[0]=[data[0]]
    for i in range(len(data)):
        x=data[i]
        if x not in list(graph.items()):
            graph[x]=[]
        for j in range(i+1, len(data)):
            diff=data[j]-x
            if diff <= 3:
                graph[x].append(data[j])
            else:
                break
    return graph

class Memoize:
    def __init__(self, fn):
        self.fn=fn
        self.memo={}

    def __call__(self, graph, root):
        if root not in self.memo:
            self.memo[root] = self.fn(graph, root)
        return self.memo[root]


@Memoize
def dfs(graph, root):
    countPaths=0
    adjlist=graph[root]
    if adjlist == []:
        return 1
    for vi in adjlist:
        countPaths+=dfs(graph, vi)
    return countPaths

def partTwo():
    with open("input.txt", "r") as inputFile:
        data=[int(x) for x in inputFile.readlines()]
        graph=makeGraph(sorted(data))
        return dfs(graph, 0)


print("Answer for part 1: ")
print(partOne())
print("Answer for part 2: ")
print(partTwo())
