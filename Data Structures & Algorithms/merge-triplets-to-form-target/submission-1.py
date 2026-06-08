class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [[a, b, c] for a, b, c in triplets if a <= target[0] and b <= target[1] and c <= target[2]]
        return any(triplet[0] == target[0] for triplet in good) and any(triplet[1] == target[1] for triplet in good) and any(triplet[2] == target[2] for triplet in good)