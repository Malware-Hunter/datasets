#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
    int counter = 0;
    char *buffer_da_linha = NULL;
    size_t n_read_chars = 0;
    size_t tamanho_alocado = 0;
    
    fprintf(stdout, "#line,n_read_chars,n_commas,n_ones,n_zeros,n_extra_white_spaces, n_other_chars\n");
    int n_commas_warning = 0;
    int n_other_chars_warning = 0;
    int n_extra_white_spaces_warning = 0;
    while ((n_read_chars = getline(&buffer_da_linha, &tamanho_alocado, stdin)) != -1) {
        int n_commas = 0, n_ones = 0, n_zeros = 0, n_other_chars = 0, n_extra_white_spaces = 0;
        ;
        for (int i = 0; i < n_read_chars; i++) {
            if (buffer_da_linha[i] == ',')
                n_commas++;
            else if (buffer_da_linha[i] == '1')
                n_ones++;
            else if (buffer_da_linha[i] == '0')
                n_zeros++;
            else if (buffer_da_linha[i] == ' ')
                n_extra_white_spaces++;
            else
                n_other_chars++;
        }
        if (n_commas_warning == 0)
            n_commas_warning = n_commas;
        else if (n_commas_warning != n_commas) {
            fprintf(stdout, "[WARNING] number of commas do not match at line %d!\n", counter);
            return -1;
        }
        if (n_other_chars_warning == 0 && counter != 0)
            n_other_chars_warning = n_other_chars;
        else if (n_other_chars_warning != n_other_chars && counter != 0) {
            fprintf(stdout, "[WARNING] number of other chars do not match at line %d!\n", counter);
            return -1;
        }
        if (n_extra_white_spaces > 0 && counter > 0)
            n_extra_white_spaces_warning += n_extra_white_spaces;
        fprintf(stdout, "%d,%ld,%d,%d,%d,%d,%d\n",
                counter,
                n_read_chars,
                n_commas,
                n_ones,
                n_zeros,
                n_extra_white_spaces,
                n_other_chars);
        counter++;
    }
    if (n_extra_white_spaces_warning > 0)
        fprintf(stdout, "%d extra white spaces found!\n", n_extra_white_spaces_warning);
    
}
