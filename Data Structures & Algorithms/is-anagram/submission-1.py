class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_a = [0]*26
        lens = len(s)
        if lens != len(t):
            return False
        for i in range(lens):
            a = ord(s[i]) - ord('a')
            b = ord(t[i]) - ord('a')
            hash_a[a] += 1
            hash_a[b] -= 1
        
        for i in hash_a:
            if i != 0:
                return False

        return True
            