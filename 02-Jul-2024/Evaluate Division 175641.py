# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        answer=[]
        for i in range(len(equations)):
            graph[equations[i][0]].append([equations[i][1],values[i]])
            graph[equations[i][1]].append([equations[i][0],1/values[i]])
        print(graph)
        def Dfs(right,left):
            stack=[(right,1)]
            visited=set()
            visited.add(right)
            while stack:
                node,val=stack.pop(-1)
                if node==left:
                    return val
                for neighbour,i in graph[node]:
                    if neighbour not in visited:
                        stack.append((neighbour,val*i))
                        visited.add((neighbour))
            return -1
        for i,j in queries:
            if i  not in graph:
                answer.append(-1)
            else:
                answer.append(Dfs(i,j))
        return answer
    
        return answer