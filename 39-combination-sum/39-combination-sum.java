class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        dfs(target, new LinkedList<Integer>(), res, candidates, 0);
        return res;
    }  
    
    private void dfs(int target, LinkedList<Integer> path, List<List<Integer>> res, int[] candidates, int start){
        if(target < 0){
            return;
        }
        if(target == 0){
            res.add(new ArrayList<Integer>(path));
            return;
        }
        // System.out.println(path.size());
        for(int i=start; i<candidates.length; i++){
            path.add(candidates[i]);
            dfs(target-candidates[i], path, res, candidates, i);
            path.remove(path.size()-1);
        }
    }
}