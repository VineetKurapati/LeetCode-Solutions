public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> set = new HashSet<int>();
        int n = nums.Length;
        for(int i = 0; i<n; i++)
        {
            int currentNumber = nums[i];
            if(set.Contains(currentNumber))
            {
                return true;
            }
            set.Add(currentNumber);
        }
        return false;
    }
}