# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent=[i for i in range(26)]
        rank=[0 for i in range(26)]
        def find(x, parent):
            if parent[x]==x:
                return x
            else:
                parent[x]=find(parent[x],parent)
                return parent[x]
        def union(x1,x2):
            p1,p2=find(x1,parent),find(x2,parent)
            if p1==p2:
                return
            if rank[p1]>rank[p2]:
                parent[p2]=parent[p1]
            elif rank[p1]<rank[p2]:
                parent[p1]=parent[p2]
            else:
                parent[p1]=parent[p2]
                rank[p2]+=1
        for i in equations:
            if i[1]=='=':
                union(ord(i[0])-ord('a'),ord(i[3])-ord('a'))
        for e in equations:
            if e[1]=='!':
                if find(ord(e[0])-ord('a'),parent)==find(ord(e[3])-ord('a'),parent):
                    return False
        return True
        