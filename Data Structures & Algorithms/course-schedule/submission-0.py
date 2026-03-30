class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)

        for pr in prerequisites:
            pr1, pr2 = pr
            prereqs[pr1].append(pr2)

        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for prereq in prereqs[course]:
                if dfs(prereq) == False:
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True

            
