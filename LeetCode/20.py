class Solution:
    def isValid(self, s: str) -> bool:
        li_first = []
        li_second = []
        li_third = []

        for i in s:
            if i == "(":
                li_first.append("(")
            elif i==")":
                if li_first:
                    li_first.pop()

            if i == "{":
                li_second.append("{")
            elif i=="}":
                if li_second:
                    li_second.pop()

            if i == "[":
                li_third.append("[")
            elif i=="]":
                if li_third:
                    li_third.pop()

        if len(li_first)==0 and len(li_second)==0 and len(li_third)==0:
            return True
        return False

            
