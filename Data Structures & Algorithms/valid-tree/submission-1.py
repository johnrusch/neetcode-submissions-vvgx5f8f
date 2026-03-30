class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        edge_map = defaultdict(list)
        for e in edges:
            e1, e2 = e
            edge_map[e1].append(e2)
            edge_map[e2].append(e1)

        state = [0] * n

        def dfs(graph_node, parent=-1):
            if state[graph_node] == 1:
                return False

            state[graph_node] = 1
            for neighbor in edge_map[graph_node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, graph_node) == False:
                    return False

            state[graph_node] = 2
            return True


        return dfs(0, -1) and all(s == 2 for s in state)