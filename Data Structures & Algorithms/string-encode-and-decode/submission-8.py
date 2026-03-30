# define a delimiter character
# for encode
#   initialize encoded string for result
#   iterate through list of strings
#   construct encoded string
#   add encoded string to result encoded string
# for decode
#   initialize decoded list for result
#   iterate through string
#   get current string length
#   add current string to decoded list


class Solution:
    

    def encode(self, strs: List[str]) -> str:
        dl = '#'
        encoded = ''

        for s in strs:
            curr = f'{len(s)}{dl}{s}'
            encoded += curr
        
        return encoded

    def decode(self, s: str) -> List[str]:
        dl = '#'
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != dl and j < len(s):
                j += 1
            curr_len = int(s[i:j])
            curr_end = (j + 1) + curr_len
            curr_str = s[j + 1:curr_end]
            decoded.append(curr_str)
            i = curr_end

        return decoded

