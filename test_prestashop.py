import requests
key = "1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL"
ENDPOINT = "http://164.92.218.36:8080/api"


#TEST call endpoint
def test_can_call_endpoint():
    response = requests.get(ENDPOINT, auth=(key,""))
    assert response.status_code == 200
    print(response.headers)
    print(response.text)
 
#------------------------------------------------ADDRESSES----------------------------------------------------

#---------------------------------------TEST view the addresses-----------------------------------------------
def test_can_get_addresses():
    response = requests.get(ENDPOINT + "/addresses", auth=(key,""))
    assert response.status_code == 200
    print(response.headers)
    print(response.text)

#-----------------------------------------TEST create an address----------------------------------------------
def test_can_create_address():
    payload = """<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id_customer></id_customer>
        <id_manufacturer></id_manufacturer>
        <id_supplier></id_supplier>
        <id_warehouse></id_warehouse>
        <id_country>1</id_country>
        <id_state></id_state>
        <alias>ola</alias>
        <company></company>
        <lastname>Yakovlieva</lastname>
        <firstname>Olha</firstname>
        <vat_number></vat_number>
        <address1>Nutona</address1>
        <address2></address2>
        <postcode></postcode>
        <city>Kharkiv</city>
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
                                            auth=(key,""))
    assert create_address_response.status_code == 201
    print(create_address_response.text)
    created_address_id = create_address_response.text.split('id')
    new_address_id = created_address_id[1].strip('>''/''<''!'']''CDATA''[')
    print(new_address_id)

#------------------------------------TEST update the address--------------------------------------------
def test_can_update_address():
#create an address
    payload = """<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id_customer></id_customer>
        <id_manufacturer></id_manufacturer>
        <id_supplier></id_supplier>
        <id_warehouse></id_warehouse>
        <id_country>1</id_country>
        <id_state></id_state>
        <alias>ola</alias>
        <company></company>
        <lastname>Yakovlieva</lastname>
        <firstname>Olha</firstname>
        <vat_number></vat_number>
        <address1>Nutona</address1>
        <address2></address2>
        <postcode></postcode>
        <city>Kharkiv</city>
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
                                            auth=(key,""))
    assert create_address_response.status_code == 201
    print(create_address_response.text)
    created_address_id = create_address_response.text.split('id')
    new_address_id = created_address_id[1].strip('>''/''<''!'']''CDATA''[')
#update the address
    new_payload = f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id>{new_address_id}</id>
        <id_customer></id_customer>
        <id_manufacturer></id_manufacturer>
        <id_supplier></id_supplier>
        <id_warehouse></id_warehouse>
        <id_country xlink:href="http://164.92.218.36:8080/api/countries/1">1</id_country>
        <id_state></id_state>
        <alias>o</alias>
        <company></company>
        <lastname>Yakovlieva</lastname>
        <firstname>Olha</firstname>
        <vat_number></vat_number>
        <address1>Socrat ave</address1>
        <address2></address2>
        <postcode></postcode>
        <city>LA</city>
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
    update_address_response = requests.put(ENDPOINT + f"/addresses/{new_address_id}", 
                                           data=new_payload, auth=(key,""))
    print(new_address_id)
    assert update_address_response.status_code == 200
    print(update_address_response.text)

#------------------------------------TEST delete the address---------------------------------------------

def test_can_delete_address():
    payload = """<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <address>
        <id_customer></id_customer>
        <id_manufacturer></id_manufacturer>
        <id_supplier></id_supplier>
        <id_warehouse></id_warehouse>
        <id_country>1</id_country>
        <id_state></id_state>
        <alias>ola</alias>
        <company></company>
        <lastname>Yakovlieva</lastname>
        <firstname>Olha</firstname>
        <vat_number></vat_number>
        <address1>Nutona</address1>
        <address2></address2>
        <postcode></postcode>
        <city>Kharkiv</city>
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
                                            auth=(key,""))
    assert create_address_response.status_code == 201
    print(create_address_response.text)
    created_address_id = create_address_response.text.split('id')
    new_address_id = created_address_id[1].strip('>''/''<''!'']''CDATA''[')
    delete_created_address = requests.delete(ENDPOINT + f"/addresses/{new_address_id}", auth=(key,""))
    assert delete_created_address.status_code == 200


#------------------------------------------------CATEGORIES--------------------------------------------------
#----------------------TEST view the categories-----------------------------------------
def test_can_get_categories():
    response = requests.get(ENDPOINT + "/categories", auth=(key,""))
    assert response.status_code == 200
    print(response.headers)
    print(response.text)

#----------------------TEST create the category----------------------------------------
def test_can_create_category():
    category_payload = """<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <category>
        <id_parent></id_parent>
        <active>0</active>
        <id_shop_default></id_shop_default>
        <is_root_category></is_root_category>
        <position></position>
        <date_add></date_add>
        <date_upd></date_upd>
        <name>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Glasses</language>
        </name>
        <link_rewrite>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
                Glasses
            </language>
        </link_rewrite>
        <description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </description>
        <meta_title>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_title>
        <meta_description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_description>
        <meta_keywords>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_keywords>
        <associations>
            <categories nodeType="category" api="categories"/>
            <products nodeType="product" api="products"/>
        </associations>
    </category>
</prestashop>
    """
    create_category_response = requests.post(ENDPOINT + "/categories", data=category_payload,                                        
                                            auth=(key,""))
    assert create_category_response.status_code == 201
    print(create_category_response.text)
    created_category_id = create_category_response.text.split('id')
    new_category_id = created_category_id[1].strip('>''/''<''!'']''CDATA''[')
    print(new_category_id)

#----------------------TEST update the category----------------------------------------
def test_can_update_category():
#create an category
    category_payload = """<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <category>
        <id_parent></id_parent>
        <active>0</active>
        <id_shop_default></id_shop_default>
        <is_root_category></is_root_category>
        <position></position>
        <date_add></date_add>
        <date_upd></date_upd>
        <name>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Glasses</language>
        </name>
        <link_rewrite>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
                Glasses
            </language>
        </link_rewrite>
        <description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </description>
        <meta_title>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_title>
        <meta_description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_description>
        <meta_keywords>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_keywords>
        <associations>
            <categories nodeType="category" api="categories"/>
            <products nodeType="product" api="products"/>
        </associations>
    </category>
</prestashop>
    """
    create_category_response = requests.post(ENDPOINT + "/categories", data=category_payload,                                        
                                            auth=(key,""))
    assert create_category_response.status_code == 201
    print(create_category_response.text)
    created_category_id = create_category_response.text.split('id')
    new_category_id = created_category_id[1].strip('>''/''<''!'']''CDATA''[')
    print(new_category_id)
#update the category
    new_category_payload = f"""<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <category>
        <id><{new_category_id}></id>
        <id_parent></id_parent>
        <active>0</active>
        <id_shop_default></id_shop_default>
        <is_root_category></is_root_category>
        <position></position>
        <date_add></date_add>
        <date_upd></date_upd>
        <name>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Shades</language>
        </name>
        <link_rewrite>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Shades</language>
        </link_rewrite>
        <description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </description>
        <meta_title>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_title>
        <meta_description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_description>
        <meta_keywords>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_keywords>
        <associations>
            <categories nodeType="category" api="categories"/>
            <products nodeType="product" api="products"/>
        </associations>
    </category>
</prestashop>
    """
    update_category_response = requests.put(ENDPOINT + f"/categories/{new_category_id}", 
                                           data=new_category_payload, auth=(key,""))
    print(new_category_id)
    assert update_category_response.status_code == 405
    print(update_category_response.text)

#----------------------TEST delete the category----------------------------------------
def test_can_delete_category():
    category_payload = """<?xml version="1.0" encoding="UTF-8"?>
<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
    <category>
        <id_parent></id_parent>
        <active>0</active>
        <id_shop_default></id_shop_default>
        <is_root_category></is_root_category>
        <position></position>
        <date_add></date_add>
        <date_upd></date_upd>
        <name>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">Glasses</language>
        </name>
        <link_rewrite>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
                Glasses
            </language>
        </link_rewrite>
        <description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </description>
        <meta_title>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_title>
        <meta_description>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_description>
        <meta_keywords>
            <language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1"></language>
        </meta_keywords>
        <associations>
            <categories nodeType="category" api="categories"/>
            <products nodeType="product" api="products"/>
        </associations>
    </category>
</prestashop>
    """
    create_category_response = requests.post(ENDPOINT + "/categories", data=category_payload,                                        
                                            auth=(key,""))
    assert create_category_response.status_code == 201
    print(create_category_response.text)
    created_category_id = create_category_response.text.split('id')
    new_category_id = created_category_id[1].strip('>''/''<''!'']''CDATA''[')
    print(new_category_id) 
    delete_created_category = requests.delete(ENDPOINT + f"/categories/{new_category_id}", auth=(key,""))
    assert delete_created_category.status_code == 405