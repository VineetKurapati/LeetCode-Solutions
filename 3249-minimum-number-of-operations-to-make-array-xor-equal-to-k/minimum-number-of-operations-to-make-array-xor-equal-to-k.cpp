class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int curr_xor = 0;
        for(auto num: nums)
        {
            curr_xor ^= num;
        }
        int count = 0;
        while (k || curr_xor)
        {
            if((k%2) != (curr_xor % 2))
            {
                count +=1;
            }
            k/=2;
            curr_xor /= 2;
        }
        return count;
    }
};