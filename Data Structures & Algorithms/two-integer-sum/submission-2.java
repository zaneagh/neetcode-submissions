class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> myMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            if(myMap.containsKey(nums[i])) {
                int[] temp = {myMap.get(nums[i]), i};
                return temp;
            }
            myMap.put(target - nums[i], i);
        }

        throw new RuntimeException();
    }
}
