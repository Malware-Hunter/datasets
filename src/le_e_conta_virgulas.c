#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    char c;
    int i = 0;
    while (!feof(stdin)) {
        int commas = 0;
        while ((c = getc(stdin)) != '\n') {
            if (c == ',') 
                commas++;
        }
        //if (commas != 24841)
        fprintf(stdout, "%d\n", commas);
    }
}

