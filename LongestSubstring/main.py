def lengthOfLongestSubstring(s):
    substring = []
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[j+1]:
                substring.append(s[i])
        return len(substring) 

lengthOfLongestSubstring("aa")
