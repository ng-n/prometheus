#include <stdio.h>
#include <cs50.h>

int main(){

    
    long cards = get_long("Number: ");
    int odd = cards%10;
    int even, res = 0;
    int starts = 0;
    int digits = 1;
    
    cards/=10;
    while(cards > 0){
        digits++;
        if(cards > 9 && cards < 100)
            starts = cards;
        if(digits%2 != 0) { 
            odd += (cards%10);
        }else{
            even = (cards%10)*2;
            if(even == 10)
                res += 1;
            else if(even > 9)
                res += (even%10) + (even/10);
                else
                    res += even;
              }
        cards /= 10;
    }
    res += odd;
    
    if((res%10 == 0 &&(digits == 15 && (starts == 34 || starts == 37))))
        printf("AMEX\n");
    else if(res%10 == 0 &&(digits == 16 && (starts > 50 && starts <56)))
            printf("MASTERCARD\n");
        else if(res%10 == 0 && ((digits == 13 || digits == 16) && ((starts/10) == 4)))
            printf("VISA\n"); 
            else  printf("INVALID\n");
    
}
