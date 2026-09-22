class Solution {
    public boolean binarySearch(int[] arr, int target){
        int l = 0;
        int r = arr.length-1;

        while(l <= r){
            int mid = l + (r - l) / 2;

            if(arr[mid] == target){
                return true;
            }

            else if(arr[mid] < target){
                l++;
            }
            else{
                r--;
            }
        }

        return false;
    }
    public boolean searchMatrix(int[][] matrix, int target) {
        int left = 0;
        int right = matrix.length-1;
        int size = matrix[0].length-1;

        while(left <= right){
            int mid = left + (right - left) / 2;

            if ((target >= matrix[mid][0]) && (target <= matrix[mid][size])){
                return binarySearch(matrix[mid], target);
            }

            else if(target < matrix[mid][0]){
                right = mid - 1;
            }

            else{
                left = mid + 1;
            }


        }

        return false;
    }
}
