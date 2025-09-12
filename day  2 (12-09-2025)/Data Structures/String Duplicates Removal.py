class Solution:
    def removeDuplicates(self, s):
        rev=[]
        for char in s:
            if char not in rev:
                rev.append(char)
        return "".join(rev)
