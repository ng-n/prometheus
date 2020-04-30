// Output:
//  *  2  3  4  * 
//  6  *  8  * 10 
// 11 12  * 14 15 
// 16  * 18  * 20 
//  * 22 23 24  * 


public class MatrixPrint {
	public static void main(String args[]){
		int size = 5;
        int cnt = 1;
        for(int i = 0; i < size; ++i){
            for(int j = 0; j < size; ++j){

                if(i == j || j == size-1-i){ 
                        System.out.print(" * ");
                }else {
                    if(cnt < 10)
                    System.out.printf(" %d ", cnt);
                else 
                    System.out.printf("%d ", cnt);
                }
                cnt++;
            }
            System.out.println();
        }
	}
}
