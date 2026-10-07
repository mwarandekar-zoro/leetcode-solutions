class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        left, right = 0, len(s) - 1
        vowels = set("aeiouAEIOU")

        while left < right:
            if s[left] not in vowels:
                left = left + 1
            elif s[right] not in vowels:
                right = right - 1
            else: 
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
        return "".join(s)
