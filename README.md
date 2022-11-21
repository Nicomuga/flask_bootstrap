#Documentación

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

Para ejecutar las migraciones el comando es el siguiente

```
flask db upgrade
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


