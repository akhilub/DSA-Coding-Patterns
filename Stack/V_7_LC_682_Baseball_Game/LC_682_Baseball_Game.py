class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for o in operations:
            match o:
                case "C":
                    stk.pop()
                case "D":
                    stk += [stk[-1]*2]
                case "+":
                    stk.append(stk[-1]+stk[-2])
                case default:
                    stk.append(int(o))
        return sum(stk) 
    

'''
Read about match here https://www.w3schools.com/python/python_match.asp
'''


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for o in operations:
            if o == "C":
                stk.pop()
            elif o == "D":
                stk += [stk[-1]*2]
            elif o == "+":
                stk.append(stk[-1]+stk[-2])
            else:
                stk.append(int(o))
        return sum(stk) 
        