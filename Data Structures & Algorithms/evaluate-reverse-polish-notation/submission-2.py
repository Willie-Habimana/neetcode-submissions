class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "/", "*", "-"}

        for token in tokens: 
            if token not in operators:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = 0
                if token == "+":
                    result = operand1 + operand2
                elif token == "-":
                    result = operand1 - operand2
                elif token == "/":
                    result = int(operand1 / operand2)
                else:
                    result = operand1 * operand2
                
                print(f"{operand1} {token} {operand2}")
                stack.append(result)
                
        
        return stack[0]


                
        