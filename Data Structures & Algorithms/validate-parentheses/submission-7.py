class Solution:
    def isValid(self, s: str) -> bool:
        res = False
        stack = []
        if s[0] == ']' or s[0] == '}' or s [0] == ')':
            return False

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                continue
            
            if len(stack) != 0:
                if stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                else:
                    return False
            elif len(stack) == 0 and (char == '}' or char == ')' or char == ']'):
                return False

        if len(stack) == 0:
            res = True

        return res