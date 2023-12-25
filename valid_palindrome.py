#https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_string = s.lower()
        alphanumeric_string = ''.join(char for char in lowercase_string if char.isalnum())
        s = alphanumeric_string
        if len(s) == 0 or s == " ":
            return True
        #print(s)
        stack = []
        queue = []
        for i in range(len(s)//2):
            stack.append(s[i]) 
            queue.append(s[len(s)-i-1])
        print(stack)
        print(queue)
        return stack == queue
