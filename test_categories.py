import requests

ENDPOINT = "http://164.92.218.36:8080/api"
key = "1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL"
new_category = """<prestashop xmlns:xlink="http://www.w3.org/1999/xlink">
<category>
<active>0</active>
<position>
<![CDATA[ 0 ]]>
</position>
<name>
<language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
<![CDATA[ korenevij-katalog ]]>
</language>
</name>
<link_rewrite>
<language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
<![CDATA[ korenevij-katalog ]]>
</language>
</link_rewrite>
<description>
<language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
<![CDATA[ ]]>
</language>
</description>
<meta_title>
<language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
<![CDATA[ ]]>
</language>
</meta_title>
<meta_description>
<language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
<![CDATA[ ]]>
</language>
</meta_description>
<meta_keywords>
<language id="1" xlink:href="http://164.92.218.36:8080/api/languages/1">
<![CDATA[ ]]>
</language>
</meta_keywords>
<associations>
<categories nodeType="category" api="categories">
<category xlink:href="http://164.92.218.36:8080/api/categories/2">
<id>
<![CDATA[ 2 ]]>
</id>
</category>
</categories>
<products nodeType="product" api="products"/>
</associations>
</category>
</prestashop>"""

def test_can_call_endpoint():
    response = requests.get(ENDPOINT, auth=(key, ""))
    assert response.status_code == 200

def test_can_get_categories():
    response = requests.get(ENDPOINT + '/categories', auth=(key,""))
    assert response.status_code == 200

def test_can_create_new_categories():
    create_categories_response = requests.post(ENDPOINT + '/categories', 
                                               auth=(key, ""), data=new_category)
    assert create_categories_response.status_code == 201
    print(create_categories_response.text)
    created_categories_id = create_categories_response.text.split('id')
    new_categories_id = created_categories_id[1].strip('>''/''<''!'']''CDATA''[')
    print(f'The id that was created is ' + new_categories_id)