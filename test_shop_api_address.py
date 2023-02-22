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
    print(response.text)


def test_can_create_new_address():
    create_address_response = requests.post(ENDPOINT + '/addresses',
                             auth=(user, password), data=new_address)
    assert create_address_response.status_code == 201
    print(create_address_response.text)
    created_address_id = create_address_response.text.split('id')
    new_address_id = created_address_id[1].strip('>''/''<''!'']''CDATA''[')
    print(f'The id that was created is ' + new_address_id)
