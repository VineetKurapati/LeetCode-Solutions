class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int n = tickets.size();
        int count = 0;
        while(tickets[k] != 0)
        {
            for(int i = 0;i<n;i++)
            {
                if(tickets[i] >= 1)
                {
                    tickets[i]-=1;
                    count +=1;
                }
                if(tickets[k] == 0)
                {
                    break;
                }
            }
        }
        return count;
    }
};