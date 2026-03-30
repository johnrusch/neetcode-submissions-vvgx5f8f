class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)

        for pr in prerequisites:
            pr1, pr2 = pr
            prereqs[pr1].append(pr2)

        state = [0] * numCourses

        res = [] 

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1
            for c in prereqs[course]:
                if dfs(c) == False:
                    current = []
                    return False

            # can't remember how to spread list into other list
            res.append(course)
            state[course] = 2

        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res
                