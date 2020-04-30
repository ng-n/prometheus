#include <cs50.h>
#include <math.h>

int main(){

    int coins = 0, cents, quarters = 25, dimes = 10 , nickels = 5, pennies = 1;
    float dollars;

    do{
        dollars = get_float("Change owed: ");
        cents = round(dollars * 100);
    }while(dollars < 0.0);

    coins += cents / quarters;
    coins += (cents % quarters) / dimes;
    coins += ((cents % quarters) % dimes) / nickels;
    coins += (((cents % quarters) % dimes) % nickels) / pennies;
    
    printf("%i\n", coins);
}
