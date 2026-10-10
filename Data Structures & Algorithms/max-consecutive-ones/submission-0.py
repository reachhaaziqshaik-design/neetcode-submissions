class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest=0
        current=0
        for i in nums:
            if i==1:
                current+=1
                longest=max(longest,current)
            else:
                current=0
        return longest