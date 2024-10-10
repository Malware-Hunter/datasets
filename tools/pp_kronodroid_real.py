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
    except BaseException as e:
        print('Exception: {}'.format(e))
        exit(1)

    print('Originals 0 >>', dataset0.shape)
    print('Originals 1 >>', dataset1.shape)
    dif = dataset0.columns.difference(dataset1.columns)

    dataset = pd.concat([dataset0, dataset1]).reset_index(drop = True)
    dataset.to_csv('kronodroid_real_device.csv', index = False)

    #remove missing values
    print_info('Remove Missing Values', 'blue')
    print_info(f'Number of Features BEFORE: {dataset.shape[1]}')
    dataset.drop(columns = ['MalFamily'], inplace = True)
    dataset.replace('None', 0, inplace = True)
    dataset.dropna(inplace = True)
    print_info(f'Number of Features AFTER: {dataset.shape[1]}')

    #remove duplicate samples
    print_info('Remove Duplicate Samples', 'blue')
    print_info(f'Number of Samples BEFORE: {dataset.shape[0]}')
    dataset.drop_duplicates(inplace = True)
    print_info(f'Number of Samples AFTER: {dataset.shape[0]}')

    #remove irrelevant features
    print_info('Remove Irrelevant Features', 'blue')
    print_info(f'Number of Features BEFORE: {dataset.shape[1]}')
    ic = get_irrelevant_columns(dataset)
    print_info(f'Number of Irrelevant Features: {len(ic)}', 'yellow')
    print(ic)
    dataset.drop(columns = ic, inplace = True)
    print_info(f'Number of Features AFTER: {dataset.shape[1]}')

    #rename class column
    print_info('Rename Class Column', 'blue')
    new_columns = list(dataset.columns)
    new_columns.remove('Malware')
    new_columns.append('class')
    dataset = dataset.rename(columns={'Malware': 'class'}).reindex(columns = new_columns)

    #cast numeric data
    print_info('Cast Numeric Data', 'blue')
    cast_to_numeric(dataset, exclude = ['Package', 'sha256', 'EarliestModDate', 'HighestModDate'])
    print('Preprocessed >>', dataset.shape)
    dataset.to_csv('preprocessing.csv', index = False)

    # generate numeral datasets
    print_info('Generate Numeral Datasets', 'blue')
    to_drop_columns = ['Package', 'sha256', 'CFileSize', 'UFileSize', 'EarliestModDate', 'HighestModDate', 'TimesSubmitted', 'Scanners']
    dataset.drop(columns = to_drop_columns, inplace = True)
    print_info(f'Continuous Dataset: {dataset.shape[0]} Samples {dataset.shape[1]} Features')
    dataset.to_csv('continuos.csv', index = False)

    to_drop_columns = ['nr_syscalls', 'nr_permissions', 'normal', 'dangerous', 'signature', 'custom_yes', 'nr_custom', 'total_perm', 'TotalIntentFilters', 'Detection_Ratio']
    dataset.drop(columns = to_drop_columns, inplace = True)
    binarize = lambda x: 0 if x <= 0 else 1
    dataset = dataset.applymap(binarize)
    print_info(f'Binary Dataset: {dataset.shape[0]} Samples {dataset.shape[1]} Features')
    dataset.to_csv('binary.csv', index = False)
    print(dataset['class'].value_counts())
