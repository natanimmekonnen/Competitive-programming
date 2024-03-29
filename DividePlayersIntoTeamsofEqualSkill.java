import java.util.Arrays;

public class DividePlayersIntoTeamsofEqualSkill {
    public long dividePlayers(int[] skill) {
        Arrays.sort(skill);
        int i=0;
        int j=skill.length -1;
        int pre=skill[0]+skill[j];
        long con=0;
        while(i<j){
            if(skill[i]+skill[j]!=pre)
                return -1;
            con+=skill[i]*skill[j];
            i++;
            j--;
        }
        return con;
    }
}
