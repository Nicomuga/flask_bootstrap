
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
flask --app <nombre_aplicacion> --debug run
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