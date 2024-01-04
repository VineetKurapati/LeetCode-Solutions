class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int>m;
        for(auto num: nums)
        {
            m[num]++;
        }
        vector<int>ans;
        priority_queue<pair<int,int>>pq;
        for(auto i : m)
        {
            pq.push({ i.second , i.first,});
        }
        while(k--)
        {
            int count = pq.top().first;
            int num = pq.top().second;
            cout<<num<<"------->"<<count<<endl;
            pq.pop();
            ans.push_back(num);
        }
        return ans;
    }
};