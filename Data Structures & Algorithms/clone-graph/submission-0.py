"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = {}

        def clone(n):
            if not n:
                return None
            if n in clone_map:
                return clone_map[n]
            copy = Node()
            copy.val = n.val
            clone_map[n] = copy
            copy.neighbors = [clone(n1) for n1 in n.neighbors]

            return copy

        return clone(node)