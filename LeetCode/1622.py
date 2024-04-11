# Wrong answer
class Fancy:

    def __init__(self):
        self.values = []

    def append(self, val: int) -> None:
        self.values.append(val)

    def addAll(self, inc: int) -> None:
        self.values = [inc+x for x in self.values]
        

    def multAll(self, m: int) -> None:
        for i in range(len(self.values)):
            self.values[i] *= m
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        return self.values[idx] % (10**9 +7)


# Given input
ops = ["Fancy","append","append","getIndex","append","getIndex","addAll","append","getIndex","getIndex","append","append","getIndex","append","getIndex","append","getIndex","append","getIndex","multAll","addAll","getIndex","append","addAll","getIndex","multAll","getIndex","multAll","addAll","addAll","append","multAll","append","append","append","multAll","getIndex","multAll","multAll","multAll","getIndex","addAll","append","multAll","addAll","addAll","multAll","addAll","addAll","append","append","getIndex"]
args = [[],[12],[8],[1],[12],[0],[12],[8],[2],[2],[4],[13],[4],[12],[6],[11],[1],[10],[2],[3],[1],[6],[14],[5],[6],[12],[3],[12],[15],[6],[7],[8],[13],[15],[15],[10],[9],[12],[12],[9],[9],[9],[9],[4],[8],[11],[15],[9],[1],[4],[10],[9]]

# Execute operations
fancy = None
output = []
for i in range(len(ops)):
    if ops[i] == "Fancy":
        fancy = Fancy()
        output.append(None)
    elif ops[i] == "append":
        fancy.append(args[i][0])
        output.append(None)
    elif ops[i] == "addAll":
        fancy.addAll(args[i][0])
        output.append(None)
    elif ops[i] == "multAll":
        fancy.multAll(args[i][0])
        output.append(None)
    elif ops[i] == "getIndex":
        output.append(fancy.getIndex(args[i][0]))

print("Output:", output)