class Solution {
public:
    bool check(string s)
    {
        int n = s.length();
        for(int i = 0;i<n/2;i++)
        {
            if(s[i] != s[n-i-1 ])
            {
                return false;
            }
        }
        return true;
    }
    bool isPalindrome(string s) {
        int n = s.length();
        string st;
        for(auto &ch:s)
        {
          if((ch>=97 && ch<=122)||(ch>=48&&ch<=57))
              st+=ch;
          else if (ch>=65 && ch <=90)
              st+=(ch+32);
        }
        return check(st);
    }
};