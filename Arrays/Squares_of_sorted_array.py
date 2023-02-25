class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        index=right
        new=[0] * len(nums)
        while index >= 0:
            if abs(nums[left]) > abs(nums[right]):
                new[index] = nums[left] * nums[left]
                left += 1
            else:
                new[index] = nums[right] * nums[right]
                right -=1
            index -= 1
        return new
