class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        book=set(nums)
        if len(book) == len(nums):
            return False
        else:
            return True