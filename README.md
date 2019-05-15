# Flask - Hello Word 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Estos son los conceptos principales que debes entender antes de hacer un Hello World en Flask:

## virtualenv: Es una herramienta para crear entornos aislados de Python.

  - Crear un entorno virtual con python3.7
  
    ```sh
      virtualenv venv --python=python3.7
    ```

  - Entrar en el entorno virtual 
  
    ```sh
      source venv/bin/activate
    ```

  - Salir del entorno virtual
  
    ```sh
      deactivate
    ```

  - **FLASK_APP**: es la variable para identificar el archivo donde se encuentra la aplicación.
  - **Debugging**: es el proceso de identificar y corregir errores de programación.
  Para activar el debug mode escribir lo siguiente en la consola:
  
    ```sh
      export FLASK_DEBUG=1
      echo $FLASK_DEBUG
    ```


## pip: Es el instalador de paquetes para Python.

  - **requirements.txt**: es el archivo en donde se colocará todas las dependencias a instalar en nuestra aplicación.

  - Instalar una libreria
  
    ```sh
      pip install <module>
    ```
    
  - Para ver las dependencias del proyecto
  
    ```sh
      pip freeze
    ```
