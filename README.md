  # Proyecto urban Grocers
  
- Este proyecto tiene como objetivo realizar pruebas automatizadas exhaustivas para 
  la aplicación Urban Grocers, centrándose en la validación del campo name durante la creación del kit de los usuarios.
  La estrategia de prueba implementada incluye tanto casos de prueba positivos como negativos. 

## Pruebas positivas:

- Verifican la funcionalidad correcta del campo name con datos de entrada válidos.

## Pruebas negativas:

- Identifican vulnerabilidades y aseguran la robustez del campo con datos inválidos o maliciosos.

## Tecnologías Utilizadas:

- Pytest: Framework de pruebas para Python.
- Requests: Biblioteca para realizar solicitudes HTTP.

## Ejecución de Pruebas:

- Para ejecutar las pruebas, se requiere tener Python instalado y los paquetes pytest y requests instalados.

## Estructura del Proyecto:

- data.py: Define los datos de prueba utilizados en las pruebas. 
- sender_stand_request.py: Realiza las solicitudes a la API de Urban Groser. 
- create_kit_name_tests.py: Combina los otros archivos para ejecutar las pruebas.
- configuration: contiene la URL del servidor y las APIS.

## Documentos utilizados:

- APIdocs.
