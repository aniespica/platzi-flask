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

## Templates

  - **Iteración**: es la repetición de un segmento de código dentro de un programa de computadora. Puede usarse tanto como un término genérico (como sinónimo de repetición), así como para describir una forma específica de repetición con un estado mutable.
  Un ejemplo de iteración sería el siguiente:
    ```sh
      {% for key, segment in segment_details.items() %}
        <tr>
          <td>{{ key }}td>
          <td>{{ segment }}td>
        tr>
      {% endfor %}  
    ```
    En este ejemplo estamos iterando por cada ```segment_details.items()``` para mostrar los campos en una tabla ```{{ key }} {{ segment }}``` de esta forma dependiendo de cuantos ```segment_details.items()``` haya se repetirá el código.

    - **Macro**: son un conjunto de comandos que se invocan con una palabra clave, opcionalmente seguidas de parámetros que se utilizan como código literal. Los Macros son manejados por el compilador y no por el ejecutable compilado.
    Los macros facilitan la actualización y mantenimiento de las aplicaciones debido a que su re-utilización minimiza la cantidad de código escrito necesario para escribir un programa.
    En este ejemplo nuestra macro se vería de la siguiente manera:

    ```sh
      {% macro nav_link(endpoint, text) %}
          {% if request.endpoint.endswith(endpoint) %}
              <li class="active"><a href="{{ url_for(endpoint) }}">{{text}}</a></li>
          {% else %}
              <li><a href="{{ url_for(endpoint) }}">{{text}}</a></li>
          {% endif %}
      {% endmacro %}
      Un ejemplo de uso de macros en Flask:
      {% from "macros.html" import nav_link with context %}
      <!DOCTYPE html>
      <html lang="en">
          <head>
          {% block head %}
              <title>My application</title>
          {% endblock %}
          </head>
          <body>
              <ul class="nav-list">
                  {{ nav_link('home', 'Home') }}
                  {{ nav_link('about', 'About') }}
                  {{ nav_link('contact', 'Get in touch') }}
              </ul>
          {% block body %}
          {% endblock %}
          </body>
      </html>
    ```
    Como podemos observar en la primera línea estamos llamando a macros.html que contiene todos nuestros macros, pero queremos uno en específico así que escribimos import ``nav_link``` para traer el macro deseado y lo renderizamos de esta manera en nuestro menú ```{{ nav_link('home', 'Home') }}```.