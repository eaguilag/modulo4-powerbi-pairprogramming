![Cata y Data: Portafolio de Vinos Españoles. Análisis y Visualización de Datos en Power BI](https://github.com/eaguilag/modulo4-powerbi-pairprogramming/header-cata-data.jpg)

# Vinos Españoles. Proyecto en Power BI.
*Equipo de desarrollo: Águila Elena [@eaguilag](https://github.com/eaguilag) y Tortarolo Franca [@FrancaTortaroloo](https://github.com/FrancaTortaroloo)*

Herramienta de visualización: Power BI

En el presente proyecto tomamos un dataset sobre vinos españoles, de la página de [Kaggle](enlace: https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset).

Está conformado por las siguientes columnas: 
1. winery: bodega
2. wine: nombre del vino
3. year: año en que se cosecharon las uvas
4. rating: calificación media del vino otorgada por los usuarios
4. num_reviews: cantidad de usuarios que dieron su opinión sobre el vino
5. country: país de origen, solamente España
6. región: región del vino
7. price: precio en euros
8. type: varidad del vino
9. body: puntaje sobre el cuerpo del vino, definido como la riqueza y la textura del vino en la boca (del 1 - 5)
10. acidity: acidez del vino, es lo que hace que un vino sea refrescante y que tu lengua quiera otro sorbo (del 1 - 5)

Dentro de ETL_Folder se encuentran 2 carpetas, `data` y `scripts`. Dentro de la carpeta `data` se encuentran otras dos más, `input data` y `output data`, en el primero se encuentra el csv original descargado de la página de Kaggle y en el segundo se encuentra el csv limpio con la información que nos resulta relevante para analizar y graficar en Power BI. Por otro lado, dentro de la carpeta `scripts` se encuentran los archivos `main.py` y `support.py`. Dentro del archivo de `main.py` se procesa los datos descargados y genera archivos limpios y transformados.


