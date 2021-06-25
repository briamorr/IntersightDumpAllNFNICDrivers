import json
import requests
from intersight_auth import IntersightAuth

def getSerial(InvDriverName,InvDriverVersion,link):
    json_body = {
        "request_method": "GET",
        "resource_path": link
    }

    RESPONSE = requests.request(
        method=json_body['request_method'],
        url=json_body['resource_path'],
        auth=AUTH
    )

    affectedDevice = RESPONSE.json()

    print(InvDriverName, InvDriverVersion, affectedDevice['Serial'], affectedDevice['Model'])

def getComponents(InvDriverName, InvDriverVersion,link):
    json_body = {
        "request_method": "GET",
        "resource_path": link
    }

    RESPONSE = requests.request(
        method=json_body['request_method'],
        url=json_body['resource_path'],
        auth=AUTH
    )
    hclStatusUrl = RESPONSE.json()
    getSerial(InvDriverVersion,InvDriverName,hclStatusUrl['ManagedObject']['link'])

    return 0

def getHCLStatus():
    components = []

    json_body = {
        "request_method": "GET",
        "resource_path": (
                'https://intersight.com/api/v1/cond/HclStatusDetails?$filter=InvDriverName eq \'nfnic\''
        )
    }

    RESPONSE = requests.request(
        method=json_body['request_method'],
        url=json_body['resource_path'],
        auth=AUTH
    )

    hclStatuses = RESPONSE.json()["Results"]

    for r in hclStatuses:
        try:
           InvDriverVersion = r['InvDriverVersion']
           InvDriverName = r['InvDriverName']
           HclStatus = r['HclStatus']
           getComponents(InvDriverName, InvDriverVersion,HclStatus['link'])

        except:
           print("")

#Configure Intersight API token and start finding all devices affected by a security advisory        
AUTH = IntersightAuth(
    secret_key_filename='SecretKey.txt',
    api_key_id='xx/xx/xx'
    )

getHCLStatus()