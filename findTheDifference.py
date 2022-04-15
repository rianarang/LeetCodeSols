class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        store = {}
        
        #add string s to hashmap
        for x in s:
            if(x not in store):
                store[x] = 1
            else:
                store[x] += 1
        
        #iterate through t to find added letter
        for x in t:
            if x in store:
                if store[x] == 0:
                    return x
                else:
                    store[x] -= 1
            else:
                return x