# Given a string s, return the longest palindromic substring in s.
# Leetcode 5

class Solution:
    def LongestPalindrome(self, s:str)-> str:
        res = ""
        resLen = 0

        # odd length of palindrome
        for i in range(len(s)):
            # we need 2 pointers
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1 ) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        # even length of palindrome
        for i in range(len(s)):
            # we need 2 pointers
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1 ) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res


sol = Solution()
print(sol.LongestPalindrome("ahphobia"))


