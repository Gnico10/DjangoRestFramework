# Django RestFramework
### Instrucciones para dar de alta servicio

1. Instalar dependencias

pip install Django==2.2.3
```
pip install python==3.7
pip install Django==2.2.3
pip install psycopg2==2.8.3
pip install djangorestframework==3.10.2
pip install django-filter==2.2.0
pip install djangorestframework_simplejwt==4.3.0
pip install django-cors-headers
```
2. Crear servidor local PostgreSQL con los siguientes datos.
    * DB: drf_api
    * USERNAME: postgres
    * PASSWORK: admin
    

3. Migrar base de datos con los siguientes comandos:
```
python manage.py makemigrations
python manage.py migrate
```

4. Correr aplicación
```
python manage.py runserver
```
