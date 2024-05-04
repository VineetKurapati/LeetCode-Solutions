class Solution {
public:
    int numRescueBoats(vector<int>& p, int limit) {
        sort(p.begin(), p.end());
        int n = p.size();
        int i = 0;
        int j = n-1;
        int boats = 0;
        while(i<=j)
        {
            boats+=1;
            if(p[i] + p[j] <= limit)
            {
                i++;
            }
            j--;
        }
        return boats;
    }
};