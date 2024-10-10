import sys
import os
import numpy as np
import pandas as pd
from utils import *

if __name__=="__main__":
    args = parse_args(sys.argv[1:])

    try:
        dataset = pd.read_csv(args.dataset, low_memory = False)
    except BaseException as e:
        print('Exception: {}'.format(e))
        exit(1)

    print('Originals >>', dataset.shape)
    #replace string 'false' or 'true' by bool 'False' or 'True'
    dataset.replace(['false', 'true'], [False, True], inplace = True)

    #remove missing values
    print_info('Remove Missing Values', 'blue')
    print_info(f'Number of Samples BEFORE: {dataset.shape[0]}')
    dataset.replace('?', np.nan, inplace = True)
    dataset.dropna(inplace = True)
    print_info(f'Number of Samples AFTER: {dataset.shape[0]}')

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
    dataset = dataset.rename(columns={'Detection Ratio': 'class'})

    #cast numeric data
    print_info('Cast Numeric Data', 'blue')
    cast_to_numeric(dataset, exclude = ['Apk Name', 'class'])
    print('Preprocessed >>', dataset.shape)
    dataset.to_csv('preprocessing.csv', index = False)

    # generate numeral datasets
    print_info('Generate Numeral Datasets', 'blue')
    dataset.drop(columns = ['Apk Name'], inplace = True)
    to_drop_columns = list(dataset.select_dtypes(include = ['int64', 'float64']).columns)
    dataset['class'] = dataset['class'].replace({'Benign' : 0, 'Malicious': 1})
    dataset.replace([False, True], [0, 1], inplace = True)

    print_info(f'Continuous Dataset: {dataset.shape[0]} Samples {dataset.shape[1]} Features')
    print('Continuous >>', dataset.shape)
    dataset.to_csv('continuos.csv', index = False)
    dataset.drop(columns = to_drop_columns, inplace = True)
    print_info(f'Binary Dataset: {dataset.shape[0]} Samples {dataset.shape[1]} Features')
    print('Binary >>', dataset.shape)
    dataset.to_csv('binary.csv', index = False)
    print(dataset['class'].value_counts())
