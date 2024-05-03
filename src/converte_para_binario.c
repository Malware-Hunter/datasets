#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv)
{
    int counter = 0, exact_number_of_commas =0;
    char *buffer_da_linha = NULL;
    size_t n_read_chars = 0;
    size_t tamanho_alocado = 0;
    if (argc < 2) {
        fprintf(stdout, "Usage: %s <exact_number_of_commas>\n", argv[0]);
        return 1;
    }
    exact_number_of_commas = atoi(argv[1]);
    // CSV file header (1st line)
    while ((n_read_chars = getline(&buffer_da_linha, &tamanho_alocado, stdin)) != -1) {
        int n_commas = 0;
        for (int i = 0; i < n_read_chars; i++) {
            if (buffer_da_linha[i] == ',')
                n_commas++;
	    }
        if (n_commas == exact_number_of_commas) {
            int value;
            char *token = strtok(buffer_da_linha, ",");
            while(token != NULL)
            {
                char _print[2] = {'1', ','};
                value = atoi(token);
                token = strtok(NULL, ",");
                if (value == 0) {
                    _print[0] = '0';
                } 
                if (token != NULL) 
                    fprintf(stdout, "%s", _print);
                else
                    fprintf(stdout, "%c", _print[0]);
            }
            fprintf(stdout, "\n");
            counter++;
        }
        if (counter % 1000 == 0) 
            fflush(stdout);
    }
}
