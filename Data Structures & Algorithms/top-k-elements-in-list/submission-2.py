class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repo = {}
        for num in nums:
            if num not in repo:
                repo[num] = 1
            else:
                repo[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in repo.items():
            buckets[value].append(key)
        
        result = []

        for bucket in reversed(buckets):
            for num in bucket:
                if len(result) >= k:
                    break
                result.append(num)
                


        return result

        

        