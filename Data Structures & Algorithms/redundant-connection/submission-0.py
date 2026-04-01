class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        
        def find(x):
            while parent[x] != x:
                x = parent[x]

            return x

        def union(x, y):
            leader_x = find(x)
            leader_y = find(y)

            if leader_x == leader_y:
                return False

            parent[leader_y] = leader_x
            return True

        for edge in edges:
            e1, e2 = edge
            if not union(e1, e2):
                return edge

            
