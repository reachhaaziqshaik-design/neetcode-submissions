class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapping=dict()
        for i in nums:
            if i in mapping:
                mapping[i]+=1
            else:
                mapping[i]=1
        result=[]
        for key in mapping:
            if mapping[key]>len(nums)//3:
                result.append(key)
        return result