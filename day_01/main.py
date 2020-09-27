class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                result.append(i)
        return result
#     pro code
#         for each in nums:
#                     idx = abs(each) - 1
#                     if nums[idx] >0:
#                         nums[idx] *= -1

#                 return [i + 1 for i in range(len(nums)) if nums[i] > 0]