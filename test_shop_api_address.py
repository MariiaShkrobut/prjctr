import requests

ENDPOINT = 'http://164.92.218.36:8080/api'
user = '1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL'
password = ''
new_address = '''<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id_customer></id_customer>
        <id_manufacturer></id_manufacturer>
        <id_supplier></id_supplier>
        <id_warehouse></id_warehouse>
        <id_country xlink:href="http://164.92.218.36:8080/api/countries/1">1</id_country>
        <id_state></id_state>
        <alias>0</alias>
        <company></company>
        <lastname>Group number two new</lastname>
        <firstname>Maks Mariia Ola</firstname>
        <vat_number></vat_number>
        <address1>123</address1>
        <address2>321</address2>
        <postcode>60000</postcode>
        <city>Morshin</city>
        <other></other>
        <phone></phone>
        <phone_mobile></phone_mobile>
        <dni></dni>
        <deleted></deleted>
        <date_add></date_add>
        <date_upd></date_upd>
    </address>
</prestashop>'''


def test_can_call_endpoint():
    response = requests.get(ENDPOINT, auth=(user, password))
    assert response.status_code == 200


def test_can_get_addresses():
    response = requests.get(ENDPOINT + '/addresses', auth=(user, password))
    assert response.status_code == 200


def test_can_create_new_address():
    create_address_response = requests.post(ENDPOINT + '/addresses',
                                            auth=(user, password), data=new_address)
    assert create_address_response.status_code == 201
    print(create_address_response.text)
    created_address_id = create_address_response.text.split('id')
    new_address_id = created_address_id[1].strip('>''/''<''!'']''CDATA''[')
    print(f'The id that was created is ' + new_address_id)


def test_can_update_the_address():
    response = requests.post(ENDPOINT + '/addresses',
                             auth=(user, password), data=new_address)
    get_id(response)
    change_address = f'''<?xml version="1.0" encoding="UTF-8"?>
        <prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
            <address>
                <id>{get_id(response)}</id>
                <id_customer></id_customer>
                <id_manufacturer></id_manufacturer>
                <id_supplier></id_supplier>
                <id_warehouse></id_warehouse>
                <id_country xlink:href="http://164.92.218.36:8080/api/countries/1">1</id_country>
                <id_state>1</id_state>
                <alias>0</alias>
                <company></company>
                <lastname>Group two Updated</lastname>
                <firstname>Mariia Ola</firstname>
                <vat_number></vat_number>
                <address1>New address</address1>
                <address2>New address2</address2>
                <postcode>70000</postcode>
                <city>Morshin</city>
                <other></other>
                <phone></phone>
                <phone_mobile></phone_mobile>
                <dni></dni>
                <deleted></deleted>
                <date_add></date_add>
                <date_upd></date_upd>
            </address>
        </prestashop>'''
    update_new_address = requests.put(
        ENDPOINT + f'/addresses/{get_id(response)}', auth=(user, password), data=change_address)
    assert update_new_address.status_code == 200
    new_lastname = str(update_new_address.text)
    new_lastname = new_lastname.split('lastname')
    new_lastname[1] = new_lastname[1].strip('>''/''<''!'']''CDATA''[')
    assert new_lastname[1] == 'Group two Updated'
    print(f'The id that was created and updated is ' + get_id(response))


def test_can_delete_the_address():
    response = requests.post(ENDPOINT + '/addresses',
                             auth=(user, password), data=new_address)
    get_id(response)
    new_address_delete = requests.delete(
        ENDPOINT + f'/addresses/{get_id(response)}', auth=(user, password))
    assert new_address_delete.status_code == 200
    print(f'The id that was deleted is ' + get_id(response))
    new_address_delete_sc = requests.get(
        ENDPOINT + f'/addresses/{get_id(response)}', auth=(user, password))
    assert new_address_delete_sc.status_code == 404
    print('The status code of deleted page is ' +
          str(new_address_delete_sc.status_code))


def get_id(to_get_address_id):
    new_address_id = str(to_get_address_id.text)
    new_address_id = new_address_id.split('id')
    new_address_id[1] = new_address_id[1].strip('>''/''<''!'']''CDATA''[')
    return new_address_id[1]
