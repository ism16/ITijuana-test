from typing import List
import csv
import _csv
import pandas as pd # type: ignore
import re
import argparse


# question 1
def search_for_text(phrase: str, text: str) -> bool:
    '''
    Write a function that takes a phrase and a text file as inputs. The function 
    returns True if the phrase is found in the document and returns False otherwise. 
    Note: Newline characters will not be included in the phrase.
    '''
    if re.findall(phrase, text.lower()):
        return True
    else:
        return False


# question 2
def read_csv(filename: str) -> List[List[str]]:
    with open(filename) as csv_file:
        reader: _csv._reader = csv.reader(csv_file, delimiter=',')
        data: List[List[str]] = [row for row in reader]
    return data


def read_csv_with_pandas(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename, header=None)


def get_column_totals(data: List[List[str]], column: int) -> float:
    total: float = sum([float(x[column]) for x in data])
    return total

def get_column_totals_from_df(data: pd.DataFrame, column: int) -> int:
    # return data.sum(axis=0)[column]
    return data.iloc[:,column].sum(axis=0) # this should be more efficient than previous line

def sum_columns_from_csv(filename: str, column: int) -> int:
    '''
    Give a Comma Separated File (csv) and a column number 
    (zero being the left most column) return the sum of all the entries in that column
    Assume that all the entries in the CSV are numbers.
    Assume also that there are no column headers

    csv library can be used for this task, but in case of a huge csv files, using pandas
    is better. Pandas is optimized for big files and also the builtin function for 
    performing operations with columns and rows
    '''
    data: pd.DataFrame = read_csv_with_pandas(filename)
    return get_column_totals_from_df(data, column)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('function', help='The function to be run (question_1 or question_2', type=str)
    parser.add_argument('arg1', help='For question_1 phrase and for question_2 filename', type=str)
    parser.add_argument('arg2', help='For question_1 text and for question_2 column', type=str)

    args = parser.parse_args()

    if args.function == 'question_1':
        print(search_for_text(args.arg1, args.arg2))
    elif args.function == 'question_2':
        print(sum_columns_from_csv(args.arg1, int(args.arg2)))
    else:
        print('Option not valid!')
