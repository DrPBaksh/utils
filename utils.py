import pandas as pd

def first_look_data(df)
    print('Number of rows : ' , len(df) )
    print('Number of columns : ' , len(df.columns) )
    print('\n  ')
    print (' Column Data types :\n', df.dtypes)
    print('\n ')
    print (' First record :\n', df.head(0))
    print('\n ')
    print(df.describe())