class Solution {
public:
    int bitwiseComplement(int n) {
        //first write number in binary
        //to flip bits xor with 1
        //convert back to decimal (remember to start at end of array bc MSD is at the end) -- pushback function casues us to be able to start from front 
        
        if(n == 0) return 1;
        
        int q = n;
        int r = 0;
        int m = 0;
        vector<int> binary;
        
        while(q != 0) {
            r = q % 2;
            q /= 2;
            m = r ^1;
            
            //add the remainder to the array and flip bit at the same time by xor with 1
            binary.push_back(m);
            
        }
        
        cout << binary[0];
        //convert back to decimal
        int ans = 0;
        int count = 1;
        int max_i = binary.size() - 1;
        for(int i = 0; i <= max_i; i++) {
            ans += count * binary[i];
            count *= 2;
        }
    
        return ans;
    }
};