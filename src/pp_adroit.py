import sys
import os
import numpy as np
import pandas as pd
from utils import *

if __name__=="__main__":
    args = parse_args(sys.argv[1:])

    try:
        dataset = pd.read_csv(args.dataset, low_memory = False, sep = ';')
    except BaseException as e:
        print('Exception: {}'.format(e))
        exit(1)

    print('Originals >>', dataset.shape)

    #remove missing values
    print_info('Remove Missing Values', 'blue')
    print_info(f'Number of Features BEFORE: {dataset.shape[1]}')

    features_nan = list()
    check_nan = dataset.isna().sum()
    for feature, value in check_nan.items():
        if value != 0:
            features_nan.append(feature)
    dataset.drop(columns = features_nan, inplace = True)
    dataset.drop(columns = ['description', 'rating_number', 'rating_count'], inplace = True)

    print_info(f'Number of Featues AFTER: {dataset.shape[1]}')

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
    dataset.drop(columns = ic, inplace = True)
    print_info(f'Number of Features AFTER: {dataset.shape[1]}')

    #rename class column
    print_info('Rename Class Column', 'blue')
    dataset = dataset.rename(columns={'LABEL': 'class'})

    #cast numeric data
    print_info('Cast Numeric Data', 'blue')
    cast_to_numeric(dataset, exclude = ['name', 'version', 'class'])
    print('Preprocessed >>', dataset.shape)
    dataset.to_csv('preprocessing.csv', index = False)

    # generate numeral datasets
    print_info('Generate Numeral Datasets', 'blue')
    dataset.drop(columns = ['name', 'version'], inplace = True)
    dataset['class'] = dataset['class'].replace({'benignware' : 0, 'malware': 1})

    print_info(f'Binary Dataset: {dataset.shape[0]} Samples {dataset.shape[1]} Features')
    print('Binary >>', dataset.shape)
    dataset.to_csv('binary.csv', index = False)
    print(dataset['class'].value_counts())
