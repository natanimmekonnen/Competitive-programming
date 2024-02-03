public class RootEqualsSumofChildren {
    public boolean checkTree(TreeNode root) {

        if(root.val==(root.right.val+root.left.val))
        {
            return true;
        }
        return false;
    }
}
