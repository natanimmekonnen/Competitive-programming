# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def init(self,accounts):
        self.size = [1 for i in range(len(accounts))]
        self.parent = [i for i in range(len(accounts))]
 
    def find(self,x):
        if self.parent[x] == x:
            return self.parent[x]

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
            
        px = self.find(x)
        py = self.find(y)

        if px != py:
            if self.size[px] > self.size[py]:
                self.size[px] += self.size[py]
                self.parent[py] = self.parent[px]
            else:
                self.size[py] += self.size[px]
                self.parent[py] = self.parent[px]
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.init(accounts)
        emailsFound = {}
        for i in range(len(accounts)):
            for k in range(1,len(accounts[i])):
                if accounts[i][k] in emailsFound:
                    self.union(i,emailsFound[accounts[i][k]])
                emailsFound[accounts[i][k]] = i

        keys = defaultdict(list)
        for i in range(len(self.parent)):
            keys[self.find(self.parent[i])].append(i)

        res = []
        for key in keys:
            temp = set()
            for i in keys[key]:
                for j in range(1,len(accounts[i])):
                    temp.add(accounts[i][j])
            l=list(temp)
            l.sort()
            l.insert(0,accounts[key][0])
            res.append(l)
        return res
        