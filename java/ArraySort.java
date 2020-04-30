// Bubble Sort
public class ArraySort {

	public static void main(String[] args) {
		int[] array = {30, 2, 10, 4, 6};
		int length = array.length;
		int tmp;

	for(int i = 0; i < length; ++i)
            for(int j = 0; j < length; ++j)
                if(array[i] < array[j]){
                    tmp = array[i];
                    array[i] = array[j];
                    array[j] = tmp;
                }
            
        for (int i = 0; i < length; i++) 
		System.out.print(array[i] + " ");	
	}
}        
		
      
