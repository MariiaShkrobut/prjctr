x = """
<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
<address>
        <id><![CDATA[1777]]></id>
        <id_customer><![CDATA[]]></id_customer>
        <id_manufacturer><![CDATA[]]></id_manufacturer>
        <id_supplier><![CDATA[]]></id_supplier>
        <id_warehouse><![CDATA[]]></id_warehouse>
        <id_country xlink:href="http://164.92.218.36:8080/api/countries/1"><![CDATA[1]]></id_country>
        <id_state><![CDATA[]]></id_state>
        <alias><![CDATA[ola]]></alias>
        <company><![CDATA[]]></company>
        <lastname><![CDATA[Yakovlieva]]></lastname>
        <firstname><![CDATA[Olha]]></firstname>
        <vat_number><![CDATA[]]></vat_number>
        <address1><![CDATA[Nutona]]></address1>
        <address2><![CDATA[]]></address2>
        <postcode><![CDATA[]]></postcode>
        <city><![CDATA[Kharkiv]]></city>
        <other><![CDATA[]]></other>
        <phone><![CDATA[]]></phone>
        <phone_mobile><![CDATA[]]></phone_mobile>
        <dni><![CDATA[]]></dni>
        <deleted><![CDATA[]]></deleted>
        <date_add><![CDATA[2023-02-18 16:43:30]]></date_add>
        <date_upd><![CDATA[2023-02-18 16:43:30]]></date_upd>
</address>
</prestashop>"""
new_address_id = x
new_address_id = new_address_id.split('id')
new_address_id[1] = new_address_id[1].strip('>''/''<''!'']''CDATA''[')
print(new_address_id[1])


def create_address(payload):
    return requests.post(ENDPOINT + "/addresses", data=payload, 
                                            headers={'Content-Type':'application/xml'}, 
                                            auth=(key,""))

def new_address_id():
    payload = """<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id_customer></id_customer>
        <id_manufacturer></id_manufacturer>
        <id_supplier></id_supplier>
        <id_warehouse></id_warehouse>
        <id_country>1</id_country>
        <id_state></id_state>
        <alias>user_alias</alias>
        <company></company>
        <lastname>user_lastname</lastname>
        <firstname>user_firstname</firstname>
        <vat_number></vat_number>
        <address1>user_address1</address1>
        <address2></address2>
        <postcode></postcode>
        <city>user_city</city>
        <other></other>
        <phone></phone>
        <phone_mobile></phone_mobile>
        <dni></dni>
        <deleted></deleted>
        <date_add></date_add>
        <date_upd></date_upd>
    </address>
</prestashop>
    """
    create_address_response = requests.post(ENDPOINT + "/addresses", data=payload, 
                                            headers={'Content-Type':'application/xml'}, 
                                            auth=(key,""))
    assert create_address_response.status_code == 201
    print(create_address_response.text)
    created_address_id = create_address_response.text.split('id')
    new_address_id = created_address_id[1].strip('>''/''<''!'']''CDATA''[')
    return new_address_id
    



  