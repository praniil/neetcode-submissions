class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                second = stack.pop()
                first = stack.pop()
                expression = f"{int(first)} {token} {int(second)}"
                result = eval(expression)
                stack.append(result)   
            else:
                stack.append(token)         

        return int(stack[-1])