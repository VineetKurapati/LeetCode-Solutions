class Solution {
public:
    map<char,string>m;
    vector<string>res;
    void helper(string digits, int i, string temp)
    {
        if(temp.length() == digits.length())
        {
            res.push_back(temp);
        }
        for(int j = 0; j<m[digits[i]].length();j++)
        {
            temp += m[digits[i]][j];
            helper(digits, i+1, temp);
            temp.pop_back();
        }
    }
    vector<string> letterCombinations(string digits) {
        if(digits.length() == 0)
        {
            return {};
        }
        m['2'] = "abc";
        m['3'] = "def";
        m['4'] = "ghi";
        m['5'] = "jkl";
        m['6'] = "mno";
        m['7'] = "pqrs";
        m['8'] = "tuv";
        m['9'] = "wxyz";
        helper(digits, 0, "");
        return res;
    }
};