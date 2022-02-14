# Valid Parentheses - Leetcode 20 
# For the solution we need the stack data structure.

# A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. 
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
 # pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

def isValid(s:str) -> bool:
    if len(s) % 2 != 0:
        return False

    stack = []
    dictCloseOpen = {"(" : ")", "[" : "]", "{" : "}"}
    
    for c in s:
        if c in dictCloseOpen:
            stack.append(c)
        else:
            if stack == []:
                return False
            a = stack.pop() # pop() – Deletes the topmost element of the stack 
            if c != dictCloseOpen[a]: 
                return False    
    return stack == []


print(isValid("()[["))