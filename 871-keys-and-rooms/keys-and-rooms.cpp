class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool>visited(n, false);
        queue<int>q;
        q.push(0);
        while(!q.empty())
        {
            int curr_room = q.front();
            q.pop();
            visited[curr_room] = true;
            for(auto key : rooms[curr_room])
            {
                if(!visited[key])
                {
                    q.push(key);
                }
            }
        }
        for(auto vis : visited)
        {
            if(!vis) return false;
        }
        return true;
    }
};