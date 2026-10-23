class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for el in tokens:
            try:
                stack.append(int(el))
                continue
            except ValueError:
                pass

            right = stack.pop()
            left = stack.pop()
            match el:
                case "+":
                    stack.append(left + right)
                case "-":
                    stack.append(left - right)
                case "*":
                    stack.append(left * right)
                case "/":
                    quotient = abs(left) // abs(right)
                    if (left < 0) != (right < 0):
                        quotient = -quotient
                    stack.append(quotient)
        return stack[-1]
        