# Módulo 4: Proyecto en Power BI

![Cata y Data: Portafolio de Vinos Españoles. Análisis y Visualización de Datos en Power BI](https://github.com/eaguilag/modulo4-powerbi-pairprogramming/tree/main/assets/header-cata-data.jpg)

# Cata & Data: Portafolio de Vinos Españoles para Sumilleres
## Análisis y Visualización en Power BI
*Equipo de desarrollo: Águila Elena [@eaguilag](https://github.com/eaguilag) y Tortarolo Franca [@FrancaTortaroloo](https://github.com/FrancaTortaroloo)*

En el presente proyecto tomamos un dataset sobre vinos españoles, de la página de [Kaggle](https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset).

Está conformado por las siguientes columnas: 

1. `winery`: bodega

2. `wine`: nombre del vino

3. `year`: año en que se cosecharon las uvas

4. `rating`: calificación media del vino otorgada por los usuarios

4. `num_reviews`: cantidad de usuarios que dieron su opinión sobre el vino

5. `country`: país de origen, solamente España

6. `region`: región del vino

7. `price`: precio en euros

8. `type`: varidad del vino

9. `body`: puntaje sobre el cuerpo del vino, definido como la riqueza y la textura del vino en la boca (del 1 - 5)

10. `acidity`: acidez del vino, es lo que hace que un vino sea refrescante y que tu lengua quiera otro sorbo (del 1 - 5)


## **1. Exploración, Limpieza y Transformación el Conjunto de Datos**

Dentro de ETL_Folder se encuentran 2 carpetas, `data` y `scripts`. Dentro de la carpeta `data` se encuentran otras dos más, `input data` y `output data`, en el primero se encuentra el csv original descargado de la página de Kaggle y en el segundo se encuentra el csv limpio con la información que nos resulta relevante para analizar y graficar en Power BI. Por otro lado, dentro de la carpeta `scripts` se encuentran los archivos `main.py` y `support.py`. Dentro del archivo de `main.py` se procesa los datos descargados y genera archivos limpios y transformados.


## **2. Identificación de Objetivos**

### Objetivo General

Portafolio interactivo en Power BI que sirve como herramienta para apoyar a sumilleres u otros profesionales especializados en la selección, recomendación y presentación de vinos durante catas y eventos.

Este conjunto de datos nos permite evaluar la calidad y la popularidad de los vinos, identificar tendencias en distintas regiones y tipos, y analizar la relación entre el precio y las calificaciones. El análisis de estos datos facilita la selección de vinos para catas y la personalización de recomendaciones atendiendo a las preferencias del público y las tendencias del mercado.

### Público Objetivo

Sumilleres especializados en la curaduría de vinos para eventos exclusivos y catas de alta gama. Sus consumidores buscan vinos de calidad, que equilibren 
prestigio y accesibilidad, con características distintivas para ocasiones especiales, así como coleccionistas y entusiastas del vino interesados en descubrir nuevas etiquetas y regiones. También va dirigido a otros profesionales, como organizadores de eventos, distribuidores de vinos y gerentes de restaurantes, que necesiten hacer una selección de vinos basándose en datos.

### Objetivos de Negocio

**1. Optimización de la Selección de Vinos:**

    - Ayudar a seleccionar los mejores vinos para diferentes tipos de eventos o públicos basados en criterios como la calidad (según las calificaciones), precio, y características sensoriales como el cuerpo y la acidez.

**2. Mejora de la Experiencia del Consumidor:**

    - Facilitar la personalización de la experiencia del consumidor al alinear las preferencias del público con los vinos disponibles, utilizando datos como la calidad y la popularidad, pero también el tipo de vino para proponer maridajes.

**3. Incentivar el Consumo Local:**

    - Proporcionar información sobre la disponibilidad de tipos de vinos según bodegas y regiones que ayuden a incentivar el consumo local y cercano.


## **3. Casos de Uso y Visualizaciones**

**Caso de Uso 1:  Preferencias Regionales**

Identificamos regiones clave en España que son conocidas por producir vinos de alta calidad. Esto es útil para planificar eventos con temas regionales o para resaltar la autenticidad de los productos ofrecidos.

![Vinos por Regiones y Bodegas](https://github.com/eaguilag/modulo4-powerbi-pairprogramming/tree/main/assets/1-vinos-regiones-bodegas.jpg)

**Caso de Uso 2: Preferencia por Años de Cosecha**

Mostramos un análisis temporal de años de cosecha en relación con la calidad percibida de los vinos, destacando años excepcionales o tendencias crecientes en ciertos tipos de vino. Esto puede ayudar a identificar vinos de cosechas especiales que podrían ser de interés particular para coleccionistas.

![Preferencias por Años de Cosecha](https://github.com/eaguilag/modulo4-powerbi-pairprogramming/tree/main/assets/2-rating-anio.jpg)


**Caso de Uso 3:  Preferencias Regionales**

Identificamos la producción de vino por regiones de España así como el tipo de vino predominante. Esto ayuda a identificar qué tipos de vino son más populares y característicos según la zona y pudiendo sugerir al consumidor una degustación de productos locales.

![Preferencias Regionales](https://github.com/eaguilag/modulo4-powerbi-pairprogramming/tree/main/assets/3-vinos-region.jpg)

**Caso de Uso 4: Calidad y Valoración de los Vinos**

Exploramos cómo la calidad (medida por las calificaciones o `rating`) se relaciona con el precio de los vinos. Este análisis ayuda a identificar vinos con alta relación calidad-precio, lo que es esencial para ofrecer recomendaciones que equilibren prestigio y accesibilidad.

![Calidad y Valoración de Tipos de Vino](https://github.com/eaguilag/modulo4-powerbi-pairprogramming/tree/main/assets/4-precio-rating-tipo.jpg)

**Caso de Uso 5: Segmentación por Perfil Sensorial**

Analizamos las características sensoriales de los vinos, como el cuerpo y la acidez, para ayudar al cliente a entender qué tipos de vinos se ajustan a ciertas preferencias de sabor o maridaje. Esto es crucial para recomendar tipos de vino que acompañen menús específicos o se ajusten a los gustos de los consumidodres.

![Segmentación por Perfil Sensorial](https://github.com/eaguilag/modulo4-powerbi-pairprogramming/tree/main/assets/5-acidez-cuerpo-tipo.jpg)

**Caso de Uso 6: Búsqueda Personalizada**

Ofrecemos la posibilidad de personalizar la búsqueda de vinos para filtrar los resultados según las necesidades del cliente. El resultado será siempre de los cinco vinos mejor valorados según la calificación y el número de opiniones. Seleccionando el vino de preferencia, destacamos sus características sensoriales y sugerimos un maridaje.

![Buscador de Vinos](https://github.com/eaguilag/modulo4-powerbi-pairprogramming/tree/main/assets/6-buscador.gif)


El [archivo de Power BI](https://github.com/eaguilag/modulo4-powerbi-pairprogramming/blob/main/dashboard_spanish_wines.pbix) está disponible en el repositorio.