class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        repo = {}

        for string in strs:
            s_str = "".join(sorted(string))

            if s_str in repo:
                repo[s_str].append(string)
            else:
                repo[s_str] = [string]
        
        return list(repo.values())