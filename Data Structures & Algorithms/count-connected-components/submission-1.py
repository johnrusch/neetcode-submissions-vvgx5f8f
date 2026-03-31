class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_dict = defaultdict(list)
        for e in edges:
            e1, e2 = e
            node_dict[e1].append(e2)
            node_dict[e2].append(e1)

        states = [0] * n


        def dfs(node):
            if states[node] != 0:
                return

            states[node] = 1
            for neighbor in node_dict[node]:
                dfs(neighbor)

            states[node] = 2
            return

        tally = 0

        for node in range(n):
            if states[node] == 0:
                dfs(node)
                tally += 1

        return tally