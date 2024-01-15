class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        map<int,vector<int>>graph;
        int n = matches.size();
        for(auto match : matches)
        {
            int winner = match[0];
            int loser = match[1];
            graph[loser].push_back(winner);
            if(graph.find(winner) == graph.end())
            {
                graph[winner] = {};
            }
        }
        vector<int>one;
        vector<int>zero;
        vector<vector<int>>res;
        for(auto player : graph)
        {
            if(player.second.size() == 0)
            {
                zero.push_back(player.first);
            }
            if(player.second.size() == 1)
            {
                one.push_back(player.first);
            }
        }
        res.push_back(zero);
        res.push_back(one);
        return res;
    }
};