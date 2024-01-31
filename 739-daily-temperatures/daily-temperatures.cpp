class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
    int n = temp.size();
    stack<pair<int, int>> st;
    st.push({temp[0], 0});
    vector<int> ans(n, 0);

    for(int i = 1; i < n; i++) {
    int t = temp[i];
    while(!st.empty() && t > st.top().first) {
        int prevIndex = st.top().second;
        st.pop();
        ans[prevIndex] = i - prevIndex;
    }
    st.push({t, i});
}


    return ans;
}
};