"""This is a very bad solution regarding time an space complexity. Please, refactor.
Check this one out, it's very clever:


def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while len(tokens) > 0:
            toke = tokens.pop(0)
            if toke == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(second+first)
            elif toke == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second-first) # The order of numbers is important
            elif toke == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(second*first)
            elif toke == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(float(second)/first)) # evaluates to a 0 with the 6/-132 scenario (as required).
            else:
                stack.append(int(toke))
        return stack.pop()
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        running_sum = 0
        def do_operation(first, second, operation):
            if operation == "+":
                return str(int(float(first) + float(second)))
            if operation == "-":
                return str(int(float(first) - float(second)))
            if operation == "*":
                return str(int(float(first) * float(second)))
            if operation == "/":
                return str(int(float(first) / float(second)))
                
        if len(tokens) < 3:
            result = tokens[0]
        elif len(tokens) == 0:
            result = 0
        else:
            counter = 1
            while len(tokens) != 1:
                for index in range(len(tokens)-2):
                    try:
                           x = float(tokens[index+2])
                    except ValueError:
                        print(f"{counter})", end="")
                        print(tokens[index], tokens[index+1], tokens[index+2])
                        result = str(do_operation(tokens.pop(index), tokens.pop(index), tokens.pop(index)))
                        tokens.insert(index, result)
                        print(f" {result}\n")
                        break
                    else:
                        continue
                counter += 1
        return int(result)


MySolution = Solution()
print(MySolution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
