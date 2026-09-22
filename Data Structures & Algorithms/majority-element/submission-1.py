class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element={}
        for i in nums:
            if i in element:
                element[i]+=1
            else:
                element[i]=1
        return max(element,key=element.get)