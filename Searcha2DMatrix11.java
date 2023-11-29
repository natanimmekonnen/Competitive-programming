public class Searcha2DMatrix11 {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row=matrix.length;
        int column=matrix[0].length;
        int i=0;
        while (i<row*column)
        {
            if(matrix[i/column][i%column]==target)
            {
                return true;
            }



            i++;
        }



        return false;
    }
}
