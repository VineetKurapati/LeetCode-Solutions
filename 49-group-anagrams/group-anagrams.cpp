class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>>m;
        for(auto str: strs)
        {
            string st = str;
            sort(st.begin(), st.end());
            m[st].push_back(str);
        }
        vector<vector<string>>res;
        for(auto i : m)
        {
            res.push_back(i.second);
        }
        return res;
    }
};