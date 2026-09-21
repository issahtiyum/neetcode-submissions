class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        repo = {}

        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in repo:
                return [repo[num2], i]
            repo[nums[i]] = i

        
        