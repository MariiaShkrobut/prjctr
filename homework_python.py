#Homework #12
print('''Hello Artem''')
result_hm12 = (2**10-16**2)/(8*32)
print("The result of homework #12 is number " + str(result_hm12).strip('.''0'))

#Homework #13
property_transfer_xml = """
<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';
//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';
//urn:multiCall/sessionId['?']</con:targetPath>
"""
result_hm13 = property_transfer_xml.split('con:targetType')
result_hm13[1] = result_hm13[1].strip('>''/''<')
print('''The result of homework #13 is word "''' + str(result_hm13[1]) + '''"''')