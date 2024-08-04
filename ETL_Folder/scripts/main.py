#%%
import support as sup
#%%
# Dataframe
ruta_input = "../data/input_data/wines_SPA.csv"
df_wines = sup.read_csv(ruta_input)
#%%
# Exploración de datos 
sup.data_exploration(df_wines)
#%%
# Reemplazar nulos de columnas categoricas a 'unknown'
nulls_cat = ["type"]
df_wines = sup.nulls_to_unknown(df_wines, nulls_cat)
#%%
# Imputacion con mediana de valores nulos en columnas numericas
nulls_num = sup.select_num_col(df_wines)
sup.impute_with_median(df_wines, nulls_num)
#%%
# Obtener el maridaje
df_wines['maridaje'] = df_wines['type'].apply(sup.obtain_pairing)
print("____________________________________________________________")
print(f"Columna de maridaje creada correctamente.")
#%%
#convertirlo a csv
ruta_output = "../data/output_data/vinos.csv"
sup.save_csv(df_wines, ruta_output)