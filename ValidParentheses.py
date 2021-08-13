class Solution:
    def isValid(self, s: str) -> bool:
        #FALSE CASES
        #empty stack but hit closing bracket
        #end of string but non empty stack
        #nonempty stack non matvhing closing brace
        stack = []
        for x in s:
            if(x == "(" or x == "[" or x == "{"):
                stack.append(x)
            elif(x == ")" or x == "}" or x == "]"):
                if(len(stack) == 0):
                    return False
                else:
                    if(x == ")" and stack[-1] == "("):
                        stack.pop()
                    elif(x == "}" and stack[-1] == "{"):
                        stack.pop()
                    elif(x == "]" and stack[-1] == "["):
                        stack.pop()
                    else:
                        return False
                    
        
        if (len(stack) == 0):
            return True
        else:
            return False
                    