class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        for i in strs:
            if "".join(sorted(i)) not in s:
                s["".join(sorted(i))]=[i]
            else:
                s["".join(sorted(i))].append(i)
        return [s[i] for i in s]