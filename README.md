
# Documentación

Esta es una aplicación web utilizando el framwork flask y bootstrap. Su proposito es ejemplificar un CRUD utilizando el recurso mensaje.
Los datos se guardan en la base de datos postgres utilizando migraciones

Las dependencias se gestionan con pipenv.

## Dependencias 

Para correr este proyecto usted necesita tener instalado python 3 y su herramienta pip.

Para revisar si las tiene instalado debe ejecutar los siguientes comandos:

```
python -V
pip -V
``` 

El resultado debe indicar un número superior a 3.
| Para instalar las dependencias debe ejecutar       `pipenv install` 

## Migraciones

Para ejecutar las migraciones el comando es el siguiente.

Para ejecutar hacia adelante:
```
flask db upgrade
```

Para ejecutar hacia atras una version previa:
```
flask db downgrade
```

En caso de modificar un modelo agregando o modificando un atributo, debemos generar una nueva migración con el comando 

```
flask db migrate -"<mensaje de la migración>"
```

**nota**: Los comandos anterioresse deben ejecutar al interior de la `pipenv shell`

## Levantando la aplicación
Para ejecutar el servidor de desarrrollo el comando es el siguiente

```
bash
pipenv shell
pipenv install
set FLASK_APP=app
set FLASK_ENV=development
flask run
```
o con la siguiente linea

```
flask --app <nombre_aplicacion> --debug run
```
Y si tiene el archivo env con las variables FLASK_DEBUG=1 y FLASK_APP=app, solo debe ejecuta el comando:

```
pipenv run flask run
```

## Blueprints

Los blueprints permiten componer aplicaciones desde componentes pequeños. Cada componente es como una mini aplicación. Permite crear aplicaciones grandes manteniendolas simples

## Modulos

Para que los blueprints esten organizados es mejor trabajarlos como módulos, es decir, que estén dentro de una carpeta.
Los módulos se pueden anidar, de hecho, nosotros hicimos el módulo `app` con su respectivo `__init__.py` y al interior tenemos otros modulos, como el modulo `messages` que además es un blueprint.

## Tarea

Crear un nuevo recurso sencillo, sin base de datos, como blueprint bajo la url `/memes`y debe renderiar un html lleno de memes

SECRET_KEY = cualquier cosa
DATABASE_URI = postgresql://muga:5543@localhost:5432/flask_bootstrap

## MVC (Model-View-Controller)

![MVC](https://cdn.educba.com/academy/wp-content/uploads/2019/04/what-is-mvc-design-pattern.jpg.webp)

Es una arquitectura para separar las responsabilidades en la manipulación de las solicitudes/respuestas(request/response).

Quien recibe las solicitudes es el Controlador o en Flask, las rutas. Los controladores se encargan de revisar que las solicitudes se cumplan con las caracteristicas necesarias para entregar una respuesta acoorde (que tenga todos los datos). 

Si el controlador lo permite, se podría, opcionalmente, llamar al modelo para obtener o modificar los datos de la BDD. Y finalmente enviuar respuesta(response) que contenga la presentacion de la aplicación. En nuestro caso, en Flask, la capa de presentación comunmente conocida como Vistas(views) se llaman Templates.

Por lo tanto, en Flask el MVC podría ser adaptado como MTR (Modelo, Template, Ruta), pero es lo mismo en términos de separar la responsabilidad.