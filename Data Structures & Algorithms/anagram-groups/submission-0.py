# initialize a dictionary
# iterate through strings
# sort each string
# use the sorted string as a key in the dictionary
# append the original string to the list associated with the sorted string
#   in the dict
# return the values of the dict as the result

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in hash_map:
                hash_map[sorted_s].append(s)
            else:
                hash_map[sorted_s] = [s]
            
        return hash_map.values()
