Proyecto de Django Prueba de backend

Descripción
Diseñar e implementar un servicio de órdenes para un restaurante que debe:
Utilizar REST.
Seguir el contrato de API especificado.


Requisitos Previos
Asegúrate de que tu computadora cumpla con los siguientes requisitos antes de comenzar:

Python instalado en tu sistema. https://www.python.org/downloads/
Pip (administrador de paquetes de Python) instalado. https://pip.pypa.io/en/stable/installation/

Instalación
Sigue estos pasos para configurar y ejecutar el proyecto en tu computadora:
* crear un directorio llamado restaurante 
* Navega al directorio del proyecto:
  cd restaurante
* Clona el repositorio desde GitHub:

git clone https://github.com/bpconnection/Prueba-de-backend.git


* Crea un entorno virtual:

python -m venv venv

* Activa el entorno virtual (en macOS o Linux):
source venv/bin/activate

O en Windows:
venv\Scripts\activate

* Instala las dependencias del proyecto:
pip install -r requirements.txt

* Configura la base de datos:
python manage.py migrate

* Ejecuta el servidor de desarrollo:
python manage.py runserver

* Abre un navegador web y visita http://localhost:8000/ para correr y acceder al proyecto.

Uso
Importar el archivo prueba_backend.postman_collection.json en postman.

Pruebas desde curl

Para llamar a cada uno de los endpoints utilizando curl, puedes seguir estos ejemplos:

1.- Crear una nueva orden (POST /order):
curl -X POST http://127.0.0.1:8000/api/order/ -H "Content-Type: application/json" -d '{
    "username": "user1",
    "text": "Una hamburguesa sin cebolla con papas fritas5",
    "ttl": 50
}'

2.- Consultar una orden por ID (GET /order/{orden_id}):
Reemplaza {orden_id} con el ID de la orden que deseas consultar.  
curl http://localhost:8000/api/order/{orden_id}/

3.- Consultar órdenes por usuario (GET /orders/{username}):
Reemplaza {username} con el nombre de usuario del cual deseas consultar las órdenes.
curl http://127.0.0.1:8000/api/orders/{username}/


Autor: Byron López