class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numset = new HashSet<Integer>();
        for(int num: nums){
            numset.add(num);
        }
        int ms = 0;
        for(int num : numset){
            if(!numset.contains(num-1)){
                int cs = 1;
                while(numset.contains(num+1)){
                    cs += 1;
                    num += 1;
                }
                ms = Math.max(cs, ms);
            }
        }
        return ms;
    }
}