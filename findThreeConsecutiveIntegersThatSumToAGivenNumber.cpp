class Solution
{
public:
    vector<long long> sumOfThree(long long num)
    {
        int mid = num % 3;
        if (mid == 0)
        {
            return vector<long long>{num / 3 - 1, num / 3, num / 3 + 1};
        }
        else
        {
            return vector<long long>{};
        }
    }
};