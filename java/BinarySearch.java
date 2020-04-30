// Binary Search

public class BinarySearch {

	public static void main(String[] args) {

	int data[] = { 3, 6, 7, 10, 34, 56, 60 };
	int numberToFind = 10;

	int l = 0;
        int r = data.length-1;
        int m;
        int f = 0;
        while(l <= r){
            m = l + (r - l)/2;
            if(data[m] == numberToFind){
                f = m;
                break;
            }
            if(data[m] < numberToFind)
                l = m + 1;
            else
                r = m - 1;
            
        }
        if(f == 0)
            System.out.print(-1);
        else
            System.out.print(f);
     }
}
