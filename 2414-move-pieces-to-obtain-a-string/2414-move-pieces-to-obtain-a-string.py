class Solution:
    def canChange(self, start: str, target: str) -> bool:

        # We want a dictionary with positions
        def process_positions(string):
            occurences = {
                'L': [],
                'R': [],
                '_': []}
            for i, symbol in enumerate(string):
                occurences[symbol].append(i)
            return occurences

        # We want to know the sequence of symbols
        def determine_seq(string):
            return string.replace('_','')

        # What is the sequence of characters?
        start_seq = determine_seq(start)
        target_seq = determine_seq(target)

        # The sequence cannot change, if it does return False
        if start_seq != target_seq:
            return False

         # How many R and L and where
        start_d = process_positions(start)
        target_d = process_positions(target)

        # We cannot make illegal moves, if it does return False
        for s, t in zip(start_d['L'], target_d['L']):
            if (t - s) > 0:
                return False

        for s, t in zip(start_d['R'], target_d['R']):
            if (t - s) < 0:
                return False

        return True