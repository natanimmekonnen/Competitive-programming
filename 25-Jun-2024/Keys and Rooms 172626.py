# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue=[]
        visited=set()
        roomlen=len(rooms)
        def bfs(rooms,node):
            visited.add(node)
            queue.append(node)
            while queue:
                node=queue.pop(0)
                for i in rooms[node]:
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)
        bfs(rooms,0)
        if len(visited)==roomlen:
            return True
        return False
        