'''Given an integer x, return true if x is a
palindrome
, and false otherwise.'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
res =  Solution()
print(res.isPalindrome(121))