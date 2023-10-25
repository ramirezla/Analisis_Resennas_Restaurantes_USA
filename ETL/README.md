<p align=center ><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **`PROYECTO FINAL GRUPO Nº 7`** </h1>

<h1 align="center">
  <span style="font-size: 20px;">@utores:  Javier Castro, Luca Ramallo, Luis Ramirez, Lesmen Garcia.</span> <br>
  <a href="https://github.com/lesmengp/Proyecto-Final-Grupo-07.git">GitHub: <span style="font-size: 20px;">Proyecto Yelp & Google Maps</span></a> <br> 
</h1>

# <h1 align=center>**`YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS`**</h1>

<p align="center">
<img src="../src/JL3 Sprint3.png", height=300>
</p>

## Sección 1
## 1. Extracción, Transformación y Carga (ETL)

### Fuente de datos
+ [DataSet de Google Maps !!!](https://drive.google.com/drive/folders/1Wf7YkxA0aHI3GpoHc9Nh8_scf5BbD4DA):  Google Drive Henry.

+ [DataSet de Yelp !!!](https://drive.google.com/drive/folders/1TI-SsMnZsNP6t930olEEWbBQdo_yuIZF):  Google Drive Henry..

### 1.1. Selección de las Categorias.


### 1.2. Carga de Datos.

Debido al gran tamaño de los archivos con los Datasets suministrados por Henry para el proyecto, se procede a separar en varios archivos, donde cada archivo contendra una cantidad de registros mas manejables en lugar de tener todos los registros en un solo archivo, en formato parquet.

#### ¿Por que formato parquet?
Parquet utiliza un formato de almacenamiento por columnas, a diferencia de CSV que es por filas, de código abierto que fue creado como parte de Apache Hadoop y en la actualidad utilizado por muchos sistemas.

Ventajas:
- Reducción del espacio de almacenamiento ya que cada columna se pueden codificar de manera independiente, con un algoritmo especifico para el tipo de dato de la columna.
- Soporta varios tipos de compresion, como Snappy o GZip, con lo cual se logra reducir aun mas el espacio de almacenamiento.
- Reduciendo el espacio de almacenamiento se reducen los costes, sobre todo al usar los almacenamientos en la nube.
- Las columnas se pueden leer de manera independiente, es decir, si solo se requieren los datos de una sola columna, se puede buscar y cargar la columna sin necesidad de cargar todas las demas columnas o datos.
- Ademas de los datos, guarda metadatos el cual contiene informacion sobre los nombres y los tipos de las columnas, estadisticas de los datos, etc.
- Estructuras anidadas con lo que es capaz de representar datos con una estructura compleja, por ejemplo, una columna puede contener a su vez otra tabla.
- Facil manipulacion de los datos como una tabla o directamente a un Dataframe.<br><br>

<p align="center"> <img src="../src/Imagenes/Parquet-FileLayout.gif", height=400> </p>
<p align="center"> <a href="https://parquet.apache.org/docs/file-format/">Esquema del formato Parquet, extraido de la documentación oficial: <span style="font-size: 20px;"></span></a> <br></p>

### Datasets desde Google Map y Yelp:

Debido al enorme tamaño de los Datasets, se considera realizar el ETL en varios pasos:<br>

1.- Se carga el Datasets original.<br>

2.- Se crean Datasets en archivos separados por grupos de registros (divide y venceras)<br>

3.- Solo se dejan en el directorio de los Datasets los archivos reducidos, por razones de espacio se eliminan los archivos con los datasets originales y los datasets intermedios.