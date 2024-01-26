#include <vector>
#include <algorithm>

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        int count = 0;

        for(int i = 0; i < n; ++i) {
            if(nums[i] == val) {
                count += 1;
            } else {
                nums[i - count] = nums[i];
            }
        }

        nums.erase(nums.end() - count, nums.end());

        return n - count;
    }
};
