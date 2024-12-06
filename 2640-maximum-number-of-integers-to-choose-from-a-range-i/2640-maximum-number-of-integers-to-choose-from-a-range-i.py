class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        numbers = set(range(1,n+1)).difference(banned)

        while sum(numbers) > maxSum:
            numbers.discard(max(numbers))
        else:
            return len(numbers)