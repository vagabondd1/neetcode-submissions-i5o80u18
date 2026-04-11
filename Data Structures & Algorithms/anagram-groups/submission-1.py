class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]

        words = dict()

        for word in strs:
            sort_word =''.join(sorted(word))
            
            if sort_word in words: 
                words[sort_word].append(word)
            else:
                words[sort_word] = [word]

        return list(words.values())