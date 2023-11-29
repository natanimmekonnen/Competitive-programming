public class RotateImage {
    public void rotate(int[][] matrix) {
        int tempo=0;
        int middlerow;
        if(matrix.length%2==0)
        { middlerow=(matrix.length/2)-1;

        }
        else {

            middlerow=matrix.length/2;


        }
        for(int i=0;i<matrix.length;i++)
        {
            for(int j=i+1;j<matrix.length;j++)
            {

                tempo= matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i]=tempo;
            }


        }
        tempo=0;

        for(int i=0;i<matrix.length;i++)
        {
            int length=matrix.length-1;
            for(int j=0;j<=middlerow;j++)
            {

                tempo= matrix[i][j];
                matrix[i][j]=matrix[i][length];
                matrix[i][length]=tempo;
                length--;
            }


        }
    }
}
