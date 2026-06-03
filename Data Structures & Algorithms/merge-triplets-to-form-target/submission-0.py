class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [t for t in triplets if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]]
        return any(t[0] == target[0] for t in good) and any(t[1] == target[1] for t in good) and any(t[2] == target[2] for t in good)
            