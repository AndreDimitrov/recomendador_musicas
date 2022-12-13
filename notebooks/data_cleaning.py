def verificar_nulos(df):
    (df.isnull().sum()/len(df)).sort_values(ascending=False)*100
    return df



def encontra_constantes(df):
    columns_to_drop_constant = []
    
    for col in df.columns:
        if df[col].nunique == 1:
            columns_to_drop_constant.append(col)
            print(f'Coluna {col} é constante.')
        else:
            continue
    
    if len(columns_to_drop_constant) > 0:
        print(f'Colunas constantes: {columns_to_drop_constant}')
        return columns_to_drop_constant
    else:
        print(f'Não tem coluna constante')
        return columns_to_drop_constant
    
    
def encontra_quasi_constantes(df):
    series_value_counts = []
    
    for col in df.columns:
        series_value_counts.append(df[col]\
                                  .value_counts(normalize=True)\
                                  .iloc[0])
    return pd.series(dict(zip(df.columns.tolist(),\
                              series_value_counts)))\
                              .sort_values(ascending=False)
    
    
    