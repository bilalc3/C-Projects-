#include <cs50.h>
#include <stdio.h>

void func (void);

int main(void)
{
    // getting the height from the users
    int height=0;
    do {
        int j = get_int ("Height:");
        height = j;
    } while (height<=0 || height>=9);


    //function for setting the spaces and dots
      for (int row = 1; row<=height; row++ ){
        int x=height-row;
        int space = 1;
        while (space<=x)
        {
            printf (" ");
            space++;
        }
        for (int y=0; y<row; y++){
        printf("#");
                 }
        printf ("  ");
         for (int z=0; z<row; z++){
        printf("#");
                 }
    printf ("\n");

    }
}