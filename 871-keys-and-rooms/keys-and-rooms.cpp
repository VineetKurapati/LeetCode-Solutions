class Solution {
public:
    void bfs(vector<vector<int>>& rooms, vector<bool>& vis, int room) {
        if (vis[room]) return;
        vis[room] = true;
        for (auto r : rooms[room]) {
            bfs(rooms, vis, r);
        }
    }

    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> vis(n, false);
        bfs(rooms, vis, 0);
        for (auto con : vis) {
            if (!con) return false;
        }
        return true;
    }
};
