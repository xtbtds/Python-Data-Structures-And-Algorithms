class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left=0
        right=len(arr)-1
        
        while left < len(arr)-1 and arr[left] < arr[left+1]:
            left+=1
            
        while right > 0 and arr[right] < arr[right-1]:
            right-=1
            
        if left == right and left != 0 and right != len(arr)-1:
            return True
        
        return False
