class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int ans = 0;
        while(tickets[k] != 0){
            for(auto &i : tickets){
                if(tickets[k] == 0) break;
                if(i != 0){
                    i--;
                    ans++;
                }
            }
        }
        return ans;
    }
};