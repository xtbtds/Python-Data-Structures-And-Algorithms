class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            temp=abs(nums[i])
            if nums[temp-1] > 0:
                nums[temp-1] = -nums[temp-1] 
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
