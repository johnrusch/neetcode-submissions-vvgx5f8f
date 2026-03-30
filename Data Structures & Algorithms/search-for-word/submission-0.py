class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        # iterate through board looking for first char of word

        def helper(word_idx, r, c):
            # checking each direction for next letter
            if word_idx == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if board[r][c] != word[word_idx]:
                return False
        
            temp = board[r][c]
            board[r][c] = '#'

            found = (helper(word_idx + 1, r - 1, c) or
                     helper(word_idx + 1, r + 1, c) or
                     helper(word_idx + 1, r, c - 1) or
                     helper(word_idx + 1, r, c + 1))

            board[r][c] = temp
            return found

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                # call helper at each char
                if helper(0, i, j): return True

        return False


        
                