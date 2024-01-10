class Solution {
public:
    void helper(int i, int j, vector<vector<char>>& grid, int n, int m)
    {
        if(i < 0 || j < 0 || i == n || j == m || grid[i][j] != '1' ) return;
        grid[i][j] = 2;
        helper(i+1, j, grid, n,m);
        helper(i, j+1, grid, n, m);
        helper(i-1, j , grid, n, m);
        helper(i, j-1, grid, n, m);

    }
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int count = 0;
        for(int i = 0; i<n ;i++)
        {
            for(int j = 0; j<m; j++)
            {
                if(grid[i][j] == '1')
                {
                    helper(i, j , grid, n, m);
                    count+=1;
                }
            }
        }
        return count;
    }
};