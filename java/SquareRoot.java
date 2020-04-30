// ax^2 + bx + c = 0

public class SquareRoot {

	public static void main(String[] args) {
		double a = 3;
		double b = 2.5;
		double c = -0.5;
		double D, x1 = 0.0, x2 = 0.0;

        if(a == 0){ 
        if(b == 0){
        System.out.println("x1=");
        System.out.println("x2=");
        }else if(c == 0){
            System.out.println("x1=" + 0.0);
            System.out.println("x2=" + 0.0);
            }
        }else{
            D = b*b - 4*a*c;
            if( D == 0)
                x1 = x2 = (-b)/(2*a);
            else if(a != 0 && D > 0){
                x1 = (-b + Math.sqrt(b*b - 4*a*c)) /(2*a);
                x2 = (-b - Math.sqrt(b*b - 4*a*c)) /(2*a); 
            }
            System.out.println("x1=" + x1);
            System.out.println("x2=" + x2);
        }
	}
}
