# Aquí pondremos las instrucciones para poder ejecutar nuestra aplicación

###########################
   PRIMERA PARTE
############################

Para crear un entorno virtual lo podemos hacer con Anaconda. Sin embargo es más recomendable hacerlo de forma manual activando VirtuaEnv. De esta manera podemos installar manualmente los paquetes que vamos necesitando y evitar entrar en conflicto con alguna libreria. Es mejor irlas instalando manualmente para que a la hora de generar el requeriments file solo contenga las librerias que hemos ido instalando a lo largo del projecto.
--------------------------------------------
1- Crear el entorno virtual

    virtualenv <nombre>
    (Para Linux y Windows es el mismo comando)
----------------------------------------------

2- Activar el entorno virtual

	Windows
		Nos posicionamos en la carpeta del proyecto
		.\env\Scripts\activate   (deactivate)
    otra forma en navegar por las carpetas y activar
		cd /env/Script/activate
	Linux
		source env/bin/activate    (deactivate)
------------------------------------------------

------------------------------------------------

3- Ahora necesitamos hacer un pip list para ver las librerias que tenemos instaladas. Deberian de aparecer solo algunas por defecto. Si lo hacemos con Anaconda aparecen muchas.

	 pip list
----------------------------------------------------

4- Ahora installamos:

    Flask
	     pip install flask
    Pandas
       pip install pandas
    Numpy
       pip install Numpy

----------------------------------------------------

5- Vuelvo a hacer pip list y deberia de aparecer Djando installado con algunas dependencias
----------------------------------------------------
6- Ahora necesito declarar las variables de entorno para correr mi aplicacion

  Windows
    set FLASK_APP = <nombre del archivo de arranque> (en este caso: main)
    set FLASK_ENV = development
  Linux
    export FLASK_APP=<nombre del archivo de arranque>


----------------------------------------------------

11- Ahora extraemos esta información para que cualquier usuario pueda utilizarla.
Esto se guarda en el archivo de requirements.
  pip freeze > requirements.txt

Si se tiene un proyecto ya comenzado y se quiere instalar las librerias del archivo:
   pip install -r requirements.txt  (o el nombre del archivo)
----------------------------------------------------
