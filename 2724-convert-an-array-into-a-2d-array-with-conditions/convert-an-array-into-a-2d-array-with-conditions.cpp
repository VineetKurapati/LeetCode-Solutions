class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        int count = 0;
        int n = nums.size();
        vector<vector<int>>v;
        while(count<n)
        {
            set<int>st;
            for(int i = 0; i<n;i++)
            {
                if(nums[i] != 0 && st.find(nums[i]) == st.end())
                {
                    st.insert(nums[i]);
                    nums[i] = 0;
                    count++;
                }
            }
            vector<int> vc(st.begin(), st.end());
            v.push_back(vc);
        }
        return v;
    }
};