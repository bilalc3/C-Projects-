#include <cs50.h>
#include <stdio.h>


int main(void)
{
    float change= 0;
    do
    {
    float j = get_float ("How much change do we owe you?\n");
     change= j;
    } while (change<=0);
    printf ("Therefore we owe you %.2f\n", change);

    // to count the number of coins we set the variables for counting
            int count_quarters= 0;
            int count_dimes = 0;
            int count_nickels = 0;
            int count_pennies = 0;

    while (change >= 0.25){
        change = change-0.25;
        count_quarters++;
    }
    while (change >= 0.10){
        change = change -0.10;
        count_dimes++;
    }
    while (change >=0.05){
        change = change -0.05;
        count_nickels++;
    }
    while (change >=0.01){
        change = change -0.01;
        count_pennies++;
    }

    int coins = count_quarters + count_dimes + count_nickels + count_pennies;
    printf ("Therefore the minimal number of coins is %i\n", coins);
}


