#import <cmath>;

class Solution
{
 /* looking at the patten, it can be seen that 
    when a number is divisible by 3 -> largest product will be all 3's
    when a number has one remainder when divided by 3 -> it is two 2's multiplied by the remainder of all 3s
    two remainder when divided by 3 -> one two multiplied by the remainder of 3's
 */
public:
    int integerBreak(int n)
    {
        if (n == 2)
            return 1;
        if (n == 3)
            return 2;

        int a = n % 3;
        int b = 0;

        if (a == 0)
        {
            b = pow(3, n / 3);
        }
        else if (a == 1)
        {
            b = pow(3, (n - 4) / 3) * 4;
        }
        else
        {
            b = pow(3, (n - 2) / 3) * 2;
        }
        return b;
    }
};