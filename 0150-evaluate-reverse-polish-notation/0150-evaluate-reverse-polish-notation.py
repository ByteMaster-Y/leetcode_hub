class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])

        for token in tokens:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand1 - operand2)
                elif token == "*":
                    stack.append(operand1 * operand2)
                elif token == "/":
                    # Python 3에서 나눗셈은 정수 나눗셈이므로 float로 형변환
                    stack.append(int(operand1 / operand2))
            else:
                # 피연산자인 경우 스택에 넣음
                stack.append(int(token))

        # 최종 결과는 스택에 남아 있는 유일한 값
        return stack[0]
