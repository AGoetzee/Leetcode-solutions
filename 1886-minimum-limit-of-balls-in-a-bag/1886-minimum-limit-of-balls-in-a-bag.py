class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def isPossible(mid):
            return sum([(i - 1) // mid for i in nums]) <= maxOperations

        low = 1
        high = max(nums)
        while low < high:
            mid = (low + high) // 2
            
            if isPossible(mid):
                high = mid
            else:
                low = mid + 1
        return low


