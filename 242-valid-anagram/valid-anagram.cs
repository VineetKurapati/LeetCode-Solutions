public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> sd = new Dictionary<char, int>();
        Dictionary<char, int> td = new Dictionary<char, int>();
        foreach (char ch in s)
        {
            if(!sd.ContainsKey(ch))
            {
                sd[ch] = 0;
            }
            sd[ch] +=1;
        }
        foreach (char ch in t)
        {
            if(!td.ContainsKey(ch))
            {
                td[ch] = 0;
            }
         
            td[ch] +=1;
        }
        foreach (char ch in s)
        {
            if(!td.ContainsKey(ch) || td[ch] != sd[ch])
            {
                return false;
            }
        }
        foreach(char ch in t)
        {
            if(!sd.ContainsKey(ch) || td[ch] != sd[ch])
            {
                return false;
            }
        }
        return true;
    }
}