import argparse
import numpy as np
import pandas as pd
from termcolor import colored, cprint

def print_info(text, color = 'green'):
    print(colored(text, color))

def parse_args(argv):
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-d', '--dataset', metavar = 'DATASET',
        help = 'Dataset (csv file).', type = str, required = True)
    parser.add_argument(
        '-s', '--sep', metavar = 'SEPARATOR',
        type = str, default = ',')
    args = parser.parse_args(argv)
    return args

def parse_args_krono(argv):
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-d', '--datasets', nargs = '+', metavar = 'DATASETS',
        help = 'Dataset (csv files).', type = str, required = True)
    args = parser.parse_args(argv)
    return args

def get_unique_values(df):
    for column_name in df.columns:
        yield (column_name, df[column_name].unique())

#returns irrelevant columns (columns with the same value in all samples)
def get_irrelevant_columns(df):
    irrelevant_columns = list()
    for column_name, unique_values in get_unique_values(df):
        if(len(unique_values) < 2):
            #print(column_name, '>>', unique_values)
            irrelevant_columns.append(column_name)
    return irrelevant_columns

def cast_to_numeric(df, exclude = list()):
    non_numeric_column = list(df.select_dtypes(exclude = ['int','float']).columns)
    for e in exclude:
        non_numeric_column.remove(e)
    for column in non_numeric_column:
        df[column] = pd.to_numeric(df[column])
