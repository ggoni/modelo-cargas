import pandas as pd


def is_outlier(df, features, times=2.5):
    '''

    Args:
    df : DatFrame. Un Pandas DataFrame.
    features: List. Contiene los features.
    times : Int. El múltiplo que se va a aplicar a IQR para establecer bordes.

    Returns:
    df: El dataframe con las columnas agregadas, indicando si es outlier en la dimension

    '''
    for feature in features:
        Q1 = df[feature].quantile(0.25)
        Q3 = df[feature].quantile(0.75)
        IQR = Q3 - Q1
        floor = max(Q1 - times * IQR, 0)
        ceiling = Q3 + times * IQR
        col_name = 'is_outlier_' + feature
        df[col_name] = (df[feature] > ceiling) | (df[feature] < floor)
    return df


def find_frequent_labels(df, var, rare_perc):
    # function finds the labels that are shared by more than
    # a certain % of the individual records  in the dataset
    
    df = df.copy()
    
    tmp = df.groupby(var)[var].count() / len(df)
    
    return tmp[tmp > rare_perc].index


'''
How to use it:

for var in vars_cat:
    # find the frequent categories
    frequent_ls = find_frequent_labels(X_train, var, 0.05)
    
    # replace rare categories by the string "Rare"
    X_train[var] = np.where(X_train[var].isin(
        frequent_ls), X_train[var], 'Rare')
    
    X_test[var] = np.where(X_test[var].isin(
        frequent_ls), X_test[var], 'Rare')
        
'''

def vars_num(df:pd.DataFrame,target:str):
    lista = [c for c in data.columns if data[c].dtypes!='O' and c!=target] # O es por 'object'
    return lista

def vars_cat(df:pd.DataFrame):
    lista = [c for c in data.columns if data[c].dtypes=='O']
    return lista


