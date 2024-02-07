class Solution {
public:
    string frequencySort(string s) {
        map<char, int> m;
        int n = s.length();
        for(int i = 0;i<n;i++)
        {
            m[s[i]]++;
        }
        priority_queue<pair<int,char>> pq;
        for(auto i: m)
        {
            pq.push({i.second, i.first});
        }
        string s1 = "";
        while(!pq.empty())
        {
            int n1 = pq.top().first;
            char ch = pq.top().second;
            pq.pop();
            while(n1--)
            {
                s1 += ch;
            }
        }
        return s1;
    }
};