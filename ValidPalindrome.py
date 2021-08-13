class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #check if character is a letter, if so put in array
        #compare index 0 to index x and so on until either one letter or no letters left, exiting if check fails
        
        letters = []
        
        ns = s.lower()
        for char in ns:
            if(char.isalnum()):
                letters.append(char)
                
        
        a = 0
        b = len(letters) - 1
        c = b//2
        while (b != c):
            if(letters[a] == letters[b]):
                a += 1
                b -= 1
            else:
                return False
            
        return True