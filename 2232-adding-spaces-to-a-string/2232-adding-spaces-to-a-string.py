class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        # Init
        sol = []

        # Apparently this is faster for lookup
        spaces = set(spaces)

        # sequentially add spaces and characters
        for i, char in enumerate(s):
            if i in spaces:
                sol.append(' ')
            sol.append(char)
        return ''.join(sol)