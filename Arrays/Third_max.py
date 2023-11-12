class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        max1=nums[0]
        max2=nums[0]
        max3=nums[0]
        for i in range(len(nums)):
            if nums[i] > max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]
            elif nums[i] < max1 and max1==max2:
                max2 = nums[i]
                max3 = nums[i]
            elif nums[i] < max1 and nums[i] > max2:
                max3 = max2
                max2 = nums[i]
            elif nums[i] < max2 and max2 == max3:
                max3 = nums[i]
            elif nums[i] < max2 and nums[i] > max3:
                max3 = nums[i]
        if max1 == max2 or max2 == max3:
            return max1
        return max3
