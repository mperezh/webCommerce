# webCommerce #

### Acerca de ###
webCommerce es una aplicacion que acerca cada usuario a nuestros clientes
  para que facilitar la eleccion de ¿A donde ir a comer?

### Usar ###
* Descargar o clonar el repositorio
* Instalar los requerimientos

    ```$ pip install -r /webCommerce/requirements.txt```
    > **NOTA:** Si se trabaja con virtualenv se debe activar el
    primero el virtualenv ```$ source ./path/bin/activate``` y 
    luego instalar los requerimientos.

* Correr el servidor

    ```$ python manage.py runserver```
  
### TODO ###
* Agregar roles a los usuarios
> Hay que hacer un modelo User o modificar el que trae Django por defecto.
MP: Me inclino por la segunda opcion.
* Hacer sistema de pago
> Crear una forma de guardar el dinero, que si un campo credito o algo asi.
* Agregar un nuevo cliente
> No se me ocurrio que otro _"cliente"_ agregar, piensen en un local o algo 
pero que no sea una empresa muy grande, nada de McDonal's ni nada parecido.
Esto es para que aparezca en la vista del index.
* Hacer vista para perfiles o modificar la vista ya existente
> Debe haber una forma de entrar a una clase de perfil de cada usuario del
sistema, cuando un cliente busque un restaurante, este debe tener una vista
donde aparezca la informacion del mismo.
