# tempo: menos de 5 minutos 
sed -i 's/0\.0/0/g' mh_100k_filtered.csv 
mv mh_100k_filtered.csv mh_100k_filtered_sed.csv

# le_e_conta_virgulas.c - menos de 5 minutos (implementacao)
gcc -o le_e_conta_virgulas le_e_conta_virgulas.c
# tempo: menos de 1 minuto (pode dar um <Ctrl-C> para interromper)
le_e_conta_virgulas < mh_100k_filtered_sed.csv > virgulas_por_linha.txt
# o valor padrao logo aparece
more virgulas_por_linha.txt

# converte_para_binario.c - 30 minutos (pesquisas, testes, implementacao, validacao)
gcc -o converte_para_binario converte_para_binario.c
# tempo: menos de 3 minutos
./converte_para_binario 24841 < mh_100k_filtered_sed.csv > mh_100k_filtered_sed_binary.csv 
