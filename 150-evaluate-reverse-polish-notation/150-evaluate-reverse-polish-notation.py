class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        
        for token in tokens:
            if token in "*/-+":
                v2 = stk.pop()
                v1 = stk.pop()
                print(token)
                if token == "*":
                    stk.append(v1*v2)
                elif token == "/":
                    stk.append(int(float(v1)/v2))
                elif token == "+":
                    stk.append(v1+v2)
                else:
                    stk.append(v1-v2)
            else:
                stk.append(int(token))
        return stk.pop()
            