class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]

        words = dict()

        for word in strs:
            words[''.join(sorted(word))] = words.get(''.join(sorted(word)),[]) + [word]

        return list(words.values())