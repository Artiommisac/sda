class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Pop the topmost element if stack is not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for the closing bracket doesn't match the stack's top
                if mapping[char] != top_element:
                    return False
            else:
                # It is an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched
        return not stack