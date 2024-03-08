class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
       map<int,int>m;
       for(auto num: nums)
       {
           m[num]++;
       } 
       vector<int>res;
       for(auto i : m)
       {
           res.push_back(i.second);
       }
        int n = res.size();
        int maxi = INT_MIN;
        for(auto num: res){
            maxi = max(num, maxi); 
        }
        int count =0;
        for(auto num: res)
        {
            if(num == maxi)
            {
                count+=num;
            }
        }
        return count;
    }
};