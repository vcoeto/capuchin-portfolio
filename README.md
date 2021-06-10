# Mongo Monkeys 
Team 4 - Capuchin Monkeys
---

##### Integrantes:
1. **
2. *Victor Coeto*
3. **

---
## 1. General Aspects

This documents serves as a guide to the implementation of a flask application to the

### 1.1 Technical requirements

* Freedom of use
* Use of Flask 


### 1.2 Structure of the files
```
- / 			    # Raíz de todo el proyecto
    - README.md		# Archivo con los datos del proyecto (este archivo)
    - Google Cloud	# Carpeta con la solución para google app engine (Web app)
    - api			# Carpeta con la solución de la API
      -static       #Frontend css
      -templates    #Frontend html and bootstrap
      -main         #Backend de flask, mongodb y redis
    - dbs			# Carpeta con los modelos, catálogos y scripts necesarios para generar las bases de datos
    - docs			# Carpeta con la documentación del proyecto
```

### 1.3 Documentation



## 2. Description



### 2.1 Casos de negocio 
    Para este proyecto se tomaron en cuenta los siguientes casos de negocio:

        * El inicio de sesión de Hospital y Gobierno al igual que el registro de cada uno 
        * El reparto de vacunas por parte del Gobierno hacia los Hospitales de su localidad 
        * Los hospitales tienen un inventario con sus vacunas utilizadas, disponiples ya apartadas y pueden acepatar el reparto que hace el gobierno sumandolas a las vacunas disponibles.
        * Los usuarios tienen la opción de llenar una forma para apartar una vacuna 

## 3. Solución

A continuación aparecen descritos los diferentes elementos que forman parte de la solución del proyecto.



### 3.2 architecture
 


### 3.3 Frontend
* Bootstrap
* HTML
* CSS
#### 3.3.1 Languges
Interaction with html, backend with python files so we execute functions.

#### 3.3.2 Framework
El framework que se usa es Flask

#### 3.3.3 Librerías de funciones o dependencias
* Flask.- el framework de donde vienen las dependecias para hacer la parte web de la aplicación
* jsonify.- Para objetos json 
* request. -pedir template 
* redirect.- mover al usuario entre los templates 
* render_template.- Loads only the HTML 
* url_for.- llamar las funciones de python en html
* session.- crear sesiones y guardar sus datos
* MongoClient.-  Conexión con mongodb
* pymongo .- Conexión con mognodb y sus operaciones dentro de él 
* ObjectId. - Se usa para identificar los objetos en html
* bycript. - Hash de passwords 
* os.- manipular los archivos.

### 3.4 API o backend

#### 3.4.1 Programming language 
Python language

#### 3.4.2 Framework
Flask framework 

#### 3.4.3 Libraries

* Flask.- el framework de donde vienen las dependecias para hacer la parte web de la aplicación
* jsonify.- Para objetos json 
* request. -pedir template 
* redirect.- mover al usuario entre los templates 
* render_template.- cargar el html 
* url_for.- llamar las funciones de python en html


# 4 Installation & Usage

Make sure you have python3 and pip installed

## Windows
Creating the virtual environment
```
py -3 -m venv python3-virtualenv

python3-virtualenv\Scripts\activate
```
After the environment was created, we need to install the necesaries dependencies
Installing the requirements
```
pip install -r requirements.txt
```
Start flask development server
```
set FLASK_ENV=development
flask run
```

## Linux 

Creating the virtual environment
```
$ python3 -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```
Installation of the dependencies

```
pip install -r requirements.txt
```
Start flask development server
```
export FlASK_ENV=development
flask run
```


## 4. References 
* https://flask-pymongo.readthedocs.io/en/latest/