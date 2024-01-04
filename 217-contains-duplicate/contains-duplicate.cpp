class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int,int>m;
        for(auto num : nums)
        {
            cout<<num<<endl;
            if(m.find(num) != m.end())
                return true;
            else
            {
                m[num]+=1;
            }
        }
        return false;
    }
};