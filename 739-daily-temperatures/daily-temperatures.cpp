class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int,int>>stack;
        int n = temperatures.size();
        stack.push({temperatures[n-1], n-1});
        vector<int>ans(n, 0);
        for(int i = n-2;i>=0;i--)
        {
            int temp = temperatures[i];
            while(!stack.empty() && stack.top().first <= temp)
            {
                stack.pop();
            }
            if(stack.empty())
            {
                ans[i] = 0;
            }
            else
            {
                int index = stack.top().second;
                ans[i] = index - i;
            }
            stack.push({temp, i});
        }
        return ans;
    }
};