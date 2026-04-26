class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False

        stack = []
        dict_el = {']': '[', '}' : '{', ')' : '('}
        
        index = 0
        while (index != len(s)):
            element = s[index]

            if element not in dict_el:
                stack.append(element)
            else:
                if len(stack) < 1 or stack[-1] != dict_el[element]:
                    return False
                stack.pop()
            index += 1
        return len(stack) == 0
