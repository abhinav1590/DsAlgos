public class program1 {
    public static void main(String[] args) {
        String specialValue = "";
        String value = "";
        String dictList[][] = { 
            {"A:1","B:2"},
            {"A:4", "C:2", "D:8", "Z:2"}
        }; 
        char keys[] = {'D','E'};
        String result[] = new String[dictList.length];

        for(int i=0; i< dictList.length ;i++){
            for(int j = 0;j < dictList[i].length; j++){
                int count = 0 ;
                char key = dictList[i][j].charAt(0);
                for(int k=0; k<keys.length; k++){
                    if(key == keys[k]){
                    specialValue = specialValue + dictList[i][j].charAt(2);
                    count++ ;
                    }
                }
                if(count != 1)
                value = value + dictList[i][j].charAt(2);
            }
            String string = specialValue + value;
            result[i] = string;
        }
        for(int a= 0;a<result.length;a++)
        System.out.print(result[a] + ' ');
    }
}
