#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main (int argc, string argv[])
{
    // checking if there is more than one values
    if (argc >= 3)
    {
        printf ("Usage: ./caesar key\n");
        return 0;
    }

    // check if key is non-integer
    for (int i = 1; i < argc; i++)
    {
        if (argv[i][i-1] >= 'a' && argv[i][i-1] <= 'z')
        {
            printf ("Usage: ./caesar key\n");
            return 0;
        }
    }

    // converting string to int
    int key_value= atoi(argv[1]);

    string plain_text = get_string ("Plain Text: ");
    int len_n = strlen(plain_text);
    printf("Encrypted Text: ");

    for (int j = 0; j < len_n; j++)
    {
        //check if the text is non alpha
        char c = plain_text[j];
        if (isalpha(plain_text[j])==0)
        {
            printf("%c", plain_text[j]);
        }
        else // check if the test is alpha
        {
            char m = 'A';
            if (islower(c))
            {
                m= 'a';
                printf ("%c", (c-m+key_value)%26+m);
            }
            else
            {
                printf("%c", (c-m +key_value)%26+m);
            }
        }


        }
        printf ("\n");

}

