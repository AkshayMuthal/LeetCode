class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        
        for token in tokens:
            if token == "*" or token == "/" or token == "+" or token == "-":
                v2 = stk.pop()
                v1 = stk.pop()
                if token == "*":
                    stk.append(v1*v2)
                if token == "/":
                    stk.append(int(float(v1)/v2))
                if token == "+":
                    stk.append(v1+v2)
                if token == "-":
                    stk.append(v1-v2)
            else:
                stk.append(int(token))
            # print(token, stk)
        return stk.pop()
            