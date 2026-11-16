class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = defaultdict(list)

        for i in strs:
            sortedI = ''.join(sorted(i))
            new[sortedI].append(i)
        return list(new.values())

