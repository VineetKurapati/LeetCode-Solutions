class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>>m;
        for(auto str: strs)
        {
            string t = str;
            sort(t.begin(), t.end());
            m[t].push_back(str);
        }
        vector<vector<string>>ans;
        for(auto i : m)
        {
            ans.push_back(i.second);
        }
        return ans;
    }
};