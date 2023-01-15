from collections import Counter 

class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    @staticmethod
    def isAnagram(s: str, t: str) -> bool:

        if(len(s)!=len(t)):
            return False

        hashmap_s = {}
        hashmap_t = {}

        for char in s:
            if  hashmap_s.get(char,-1) == -1:
                hashmap_s[char]=1
            else:
                hashmap_s[char]+=1

        for char in t:
            if  hashmap_t.get(char,-1) == -1:
                hashmap_t[char]=1
            else:
                hashmap_t[char]+=1

        if len(dict.keys(hashmap_s)) != len(dict.keys(hashmap_t)):
            return False

        else:
            for char in hashmap_s:
                ct = hashmap_t.get(char,-1)
                if ct == -1 or ct != hashmap_s[char]:
                    return False 
                
            return True


data = Solution.isAnagram("anagram","nagaram")
print(data)