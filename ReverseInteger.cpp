class Solution {
public:
    int reverse(int x) {
        //how to fix if reversed int no longer int
        
        if(x < INT_MIN || x >= (INT_MAX - 1)) return 0;
        if(x == -2147483648) return 0;
        //last digit
        int ld = 0;
        //reversed number
        int r = 0;
        if(x < 0)
        {
            x *= -1;
                while(x > 0)
            {
                if(r > INT_MAX/10.0) return 0;
                else
                {
                    ld = x%10;
                    r = r*10 + ld;
                    x /= 10;
                }
                
            }
            
            r *= -1;
        
        }
        else
       { 
            while(x > 0)
            {
                if(r > INT_MAX/10.0) return 0;
                else
                {
                    ld = x%10;
                    r = r*10 + ld;
                    x /= 10;
                }
                
            }
            
        }
        return r;
    }
};
