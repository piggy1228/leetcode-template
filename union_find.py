#disjoit union set  模版
class DUS:
    def __init__(self, n):  # disjoint union set 模板，请参考花花酱视频
        self.parent = [i for i in range(n)]
        self.counts = [0 for i in range(n)]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def merge(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if self.counts[px] < self.counts[py]:
            self.parents[px] = py
        elif  self.counts[px] > self.counts[py]:
            self.parents[py] = px
        else:
            self.parents[px] = py
            self.counts[x] +=1


    # [a==b,b==c,c==d]
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        #all the possibility
        uf = {a: a for a in string.lowercase}

        for a,e,_,b in equations:
            if e == "=":
                uf[find(a)] = find(b)
        #print uf
        for a,e,_,b in equations:
            if e == "!":
                if find(a) == find(b):
                    return False
        return True
