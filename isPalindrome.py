class Solution:
    def isPalindrome(self, x: int) -> bool:
        # first put number into array
        # compare indicies of said array (last to first and so on)
        # will be diff if number is even/odd
        # base cases/ edge cases 1 digit number is true

        l = len(str(x))

        if(l == 1):
            return True

        if(x < 0):
            return False

        temp = x
        arr = []

        while(temp/10 != 0):
            arr.append(temp % 10)
            temp /= 10

        arr.append(temp)
        count = 0

        print(arr)

        while(count < l):
            if(arr[count] != arr[l-count]):
                return False
            count += 1

        return True
