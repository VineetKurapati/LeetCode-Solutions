class Solution {
public:
    int findPivot(vector<int>& nums){
        int start = 0;
        int end = nums.size() - 1;
        int mid = 0;

        while(start <= end){
            int mid = start + (end-start)/2;

            //Not Rotated
            if(nums[start] < nums[end]) return (nums.size()-1);


            //Rotated
            if(mid == 0){
                return 0;
            }

            if(mid == nums.size()-1){
                return (nums.size()-1);
            }

            if(nums[mid] > nums[mid+1]){
                return mid;
            }
            else if(nums[mid] > nums[end]){
                // Highest Number is present in right subarray
                start = mid;
            }
            else if(nums[mid] < nums[end]){
                // Highest number is present in left subarray
                end = mid;
            }
        }
        return -1;
    }

    int findMin(vector<int>& nums) {
        int pivot = findPivot(nums);
        cout << pivot;
        int index = (pivot+1)%(nums.size());
        int ans = nums[index];
        return ans;
    }
};