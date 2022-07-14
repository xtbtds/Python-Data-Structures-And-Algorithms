#RECURSIVE WITH MEMOIZATION
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:              
        resultRow = []
        for i in range(rowIndex+1):        
            resultRow.append(self.countNumber(rowIndex, i, cache = {}))
        return resultRow

    def countNumber(self, rowIndex, i, cache = {}):
        if (rowIndex, i) in cache.keys():
            return cache[(rowIndex, i)]
        if i < 0 or rowIndex < 0:
            return 0
        if i == 0 and rowIndex == 0:
            return 1
        else:
            res = self.countNumber(rowIndex-1, i, cache) + self.countNumber(rowIndex-1, i-1, cache)
            cache[(rowIndex, i)] = res
            return res

#ITERATIVE
