class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repo = {}
        for num in nums:
            if num not in repo:
                repo[num] = 1
            else:
                repo[num] += 1
        
        arranged = sorted(repo, key= lambda x: repo[x])

        return arranged[len(arranged) - k:]

        

        