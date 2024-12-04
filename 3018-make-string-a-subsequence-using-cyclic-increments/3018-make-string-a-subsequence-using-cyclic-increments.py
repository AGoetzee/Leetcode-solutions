class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Create a wrap function, we will need it later
        wrap = lambda x: ord('a') if x > ord('z') else x

        # Get ascii values for str2
        ord_str2 = [ord(i) for i in str2]
        
        # Initialize
        sub = [0 for i in ord_str2] # Keep track of ordinals
        i = 0 # Pointer for str2
        for char in str1:
            
            # If we have the char, or it can be cycled, add it
            if ord(char) == ord_str2[i] or wrap(ord(char) + 1) == ord_str2[i]:
                sub[i] = ord_str2[i]
                i += 1 # Move the pointer

            # If we are at the end of str2, break
            if i == len(ord_str2):
                break
        
        # Final check, do we have a subsequence?
        if sub == ord_str2:
            return True
        return False