# web-personal-2021
Proyecto web para entender como funciona la web y como funciona Django.


cree el entorno
lo active

Clonar repo
entre
django-admin startproject ...name
moverse a la altura del archivo manage.py
python manage.py runserver 

python manage.py makemigrations 
python manage.py migrate

django-admin startapp core
la agregamos al settings.py INSTALLED_APPS
crear la vista
agregar al urls.py

python manage.py createsuperuser
localhost/admin

## Tarea

crear las vistas de:
- about
- portfolio
- contact

## instalar docker y docker-compose

crear imagen a partir de un dockerfile
    docker build <opcional --tag para asignar etiqueta> .

con el docker-compose.yml creado levantamos
    docker-compose -f docker-compose.yml up < -d para correr en background>
