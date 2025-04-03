import requests
import configuration
import data


#CREAR UN USUARIO
def post_new_user(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

#CREAR UN KIT
def post_kid_new(kit_body):
    headers = {'Content-Type': 'application/json',  # Asegúrate de incluir el Content-Type si es necesario
               'Authorization': f"Bearer {data.Bearer_Token}"}
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)

response = post_kid_new(data.kit_body)
print(response.status_code)
print(response.json())
