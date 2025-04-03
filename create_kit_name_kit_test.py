import data
import sender_stand_request



def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["Name"] = name
    return current_kit_body


 #pruebas positivas
def positive_assert(kit_body):
    user_kit_body = get_kit_body(kit_body)
    user_response = sender_stand_request.post_kid_new(user_kit_body)

    assert user_response.status_code == 201

#pruebas negativas
def negative_assert_code_400(kit_body):
    user_kit_body = get_kit_body(kit_body)
    response = sender_stand_request.post_kid_new(user_kit_body)
    assert response.status_code == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos. " \


#puebas positivas
def test1_create_user_1_letter_in_name_get_success_response():
    positive_assert("a")


def test2_create_user_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test3_create_user_special_characters_in_name_get_success_response():
    positive_assert("\"№%@\",")

def test4_create_user_space_in_name_get_success_response():
    positive_assert( " A Aaa " )

def test5_create_user_numbers_in_name_get_success_response():
    positive_assert("123")

#pruebas negativas
def test6_create_user_has_empty_characters_in_name_get_error_response():
    negative_assert_code_400("")


def test7_create_user_512_letter_in_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


def test8_create_user_has_no_name_in_kit_body_get_error_response():
    negative_assert_code_400("name")


def test9_create_user_number_type_name_get_error_response():
    kit_body = get_kit_body(123)

    response = sender_stand_request.post_kid_new(kit_body)
    assert response.status_code == 400
