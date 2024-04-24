import sys
import os
import numpy as np
import pandas as pd
from utils import *

if __name__=="__main__":
    args = parse_args_krono(sys.argv[1:])

    try:
        dataset0 = pd.read_csv(args.datasets[0], low_memory = False)
        dataset1 = pd.read_csv(args.datasets[1], low_memory = False)
        dataset2 = pd.read_csv(args.datasets[2], low_memory = False)
    except BaseException as e:
        print('Exception: {}'.format(e))
        exit(1)

    print('Original Permissions >>', dataset0.shape)
    print('Originals Receivers >>', dataset1.shape)
    print('Originals Services >>', dataset2.shape)

    dataset0 = dataset0.rename(columns = lambda x: x.replace('permission.', ''))
    dataset0.drop(columns = ['class'], inplace = True)
    dataset0 = dataset0.add_prefix('permission :: ')

    dataset1.drop(columns = ['class'], inplace = True)
    dataset1 = dataset1.add_prefix('receiver :: ')

    #dataset2.drop(columns = ['service.LocalService'], inplace = True)
    dataset2 = dataset2.rename(columns = lambda x: x.replace('service.', ''))
    dataset2 = dataset2.add_prefix('service :: ')
    dataset2.rename(columns = {'service :: class': 'class'}, inplace = True)

    dataset = pd.concat([dataset0, dataset1, dataset2], axis = 1)
    dataset.to_csv('defensedroid_prs.csv', index = False)

    #remove missing values
    print_info('Remove Missing Values', 'blue')
    print_info(f'Number of Samples BEFORE: {dataset.shape[0]}')
    dataset.dropna(inplace = True)
    print_info(f'Number of Samples AFTER: {dataset.shape[0]}')

    #remove duplicate samples
    print_info('Remove Duplicate Features', 'blue')
    print_info(f'Number of Features BEFORE: {dataset.shape[1]}')
    duplicated_cols = dataset.columns.duplicated()
    #print(f'Colunas Duplicadas: {dataset.columns[duplicated_cols]}')
    print_info(f'Number of Duplicated Features: {list(duplicated_cols).count(True)}', 'yellow')
    dataset = dataset.loc[:, ~duplicated_cols]
    #dataset.drop_duplicates(inplace = True)
    print_info(f'Number of Features AFTER: {dataset.shape[1]}')

    #remove irrelevant features
    print_info('Remove Irrelevant Features', 'blue')
    print_info(f'Number of Features BEFORE: {dataset.shape[1]}')
    ic = get_irrelevant_columns(dataset)
    #print(ic)
    print_info(f'Number of Irrelevant Features: {len(ic)}', 'yellow')
    dataset.drop(columns = ic, inplace = True)
    dataset.drop(columns = ['permission :: '], inplace = True)
    print_info(f'Number of Features AFTER: {dataset.shape[1]}')

    #cast numeric data
    print_info('Cast Numeric Data', 'blue')
    cast_to_numeric(dataset)
    print('Preprocessed >>', dataset.shape)
    dataset.to_csv('preprocessing.csv', index = False)

    # generate numeral datasets
    print_info('Generate Numeral Datasets', 'blue')
    print_info(f'Binary Dataset: {dataset.shape[0]} Samples {dataset.shape[1]} Features')
    print('Binary >>', dataset.shape)
    dataset.to_csv('binary.csv', index = False)
    print(dataset['class'].value_counts())
