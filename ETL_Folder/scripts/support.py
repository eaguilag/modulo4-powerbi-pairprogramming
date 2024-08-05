#%%
import pandas as pd
import numpy as np
#%%
# Leer CSV
def read_csv(path):
    df = pd.read_csv(path)
    return df
#%%
# Exploracion de datos
def data_exploration(df):
    print('_____________ INFORMACIÓN GENERAL DEL DATAFRAME ____________\n')
    print(df.info())
    print('___________________ FORMA DEL DATAFRAME ____________________\n')   
    print(f"El número de filas que tenemos es de {df.shape[0]}.\nEl número de columnas es de {df.shape[1]}\n")
    print('_______________ NULOS, ÚNICOS Y DUPLICADOS _________________\n')   
    print('El porcentaje de valores NULOS por columna es de:\n')
    print((df.isnull().sum() / len(df)) * 100)
    print('____________________________________________________________\n')
    print('La cantidad de valores ÚNICOS por columna es de:\n')      
    for columna in df.columns:
        cantidad_valores_unicos = len(df[columna].unique())
        print(f'La columna {columna}: {cantidad_valores_unicos}')
    print('____________________________________________________________\n')
    print('La cantidad de valores DUPLICADOS es:\n')
    print(df[columna].duplicated().sum())
    print('\n____________________ RESUMEN ESTADÍSTICO ____________________')
    print('____________________ Variables Numéricas __________________\n')
    print(df.describe().T)    
    print('___________________ Variables Categóricas _________________\n')
    print(df.describe(include='object').T)
#%%
# Eliminar registros duplicados
def detele_duplicates(df):
    print("____________________________________________________________")
    # Elimino duplicados si los hay
    if df.duplicated().any():
        print(f"Hay {df.duplicated().sum()} registros duplicados encontrados y eliminados.")
        df = df.drop_duplicates(keep='first')
    else:
        print("No se encontraron duplicados.")
    return df
#%%
# Reemplazar nulos de columnas categoricas a 'Unknown'
def nulls_to_unknown(df, columnas):
    print("____________________________________________________________")
    for columna in columnas:
        df[columna] = df[columna].fillna('Unknown')
    # Verificamos si quedan nulos en las columnas especificadas
    nulos_restantes = df[columnas].isnull().sum()
    print("Después del reemplazo usando 'fillna' quedan los siguientes nulos:")
    print(nulos_restantes)
    return df
#%%
# Seleccion columnas numericas con nulos
def select_num_col(df):
    nulls_cols = df.columns[df.isnull().any()]
    nulls_num = df[nulls_cols].select_dtypes(include=np.number).columns
    return nulls_num
#%%
# Imputacion con mediana de valores nulos en columnas numericas
def impute_with_median (df,cols):
    print("____________________________________________________________")
    for col in cols:
        mediana = df[col].median()
        df[col].fillna(mediana, inplace=True)
    # Comprobar los nulos para cada columna específica
    for col in cols:
        print(f"Después del 'fillna' la columna {col.upper()} tiene {df[col].isnull().sum()} nulos")       
    return df
#%%
# Obtener el maridaje
def obtain_pairing(type):
    pairings = {
        'Ribera Del Duero Red': 'Carnes rojas, cordero',
        'Rioja Red': 'Carnes rojas, caza, quesos',
        'Priorat Red': 'Carnes rojas, guisos',
        'Red': 'Carnes, pastas, quesos',
        'Unknown': 'unknown',
        'Toro Red': 'Carnes rojas, embutidos',
        'Tempranillo': 'Carnes rojas, quesos curados',
        'Sherry': 'Aperitivos, sopas, mariscos',
        'Rioja White': 'Pescados, mariscos, arroces',
        'Pedro Ximenez': 'Postres, quesos azules',
        'Grenache': 'Carnes blancas, quesos suaves',
        'Albarino': 'Mariscos, pescados, arroces',
        'Cava': 'Aperitivos, mariscos, postres',
        'Verdejo': 'Pescados, mariscos, ensaladas',
        'Monastrell': 'Carnes rojas, embutidos',
        'Mencia': 'Carnes, guisos, embutidos',
        'Montsant Red': 'Carnes rojas, caza',
        'Syrah': 'Carnes rojas, caza, quesos',
        'Chardonnay': 'Pescados, aves, quesos',
        'Cabernet Sauvignon': 'Carnes rojas, caza, quesos',
        'Sparkling': 'Aperitivos, postres, mariscos',
        'Sauvignon Blanc': 'Pescados, mariscos, ensaladas'
    }
    return pairings.get(type, 'unknown')
#%%
# Guardar CSV
def save_csv(df,path):
    df.to_csv(path, index=False)
    print("____________________________________________________________")
    print(f"Dataframe guardado correctamente.")
    return df