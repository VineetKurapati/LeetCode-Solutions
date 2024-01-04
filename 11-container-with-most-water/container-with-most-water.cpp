class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int n = height.size();
        int j = n-1;
        int g_max = 0;
        while(i<j)
        {
            int curr = min(height[i],height[j]) * (j-i);
            g_max = max(curr, g_max);
            if(height[i] < height[j])
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return g_max;
    }
};