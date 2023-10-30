import pandas
import openpyxl as df
import json
import requests
get = pandas.read_excel('WEBSITES_DB.xlsx')


json_str = get.to_json(orient='records')
list_var = json.loads(json_str)
# print(list_var)
def listArr():
    newArray = []
    for i in list_var:
        # print(i['domain 2'])
        if i['domain_initial'] != None:
            
            obj = {'name': i['project_name'], 'url': i['domain_initial']}
            # req = requests.get(obj['url'])
            # print(req.status_code, 'domain_initial')
            # if req.status_code == 200:

                # newArray.append(obj)
            newArray.append(obj)
            
        if i['domain 2'] != None:
            obj = {'name': i['project_name'],'url': i['domain 2'] }
            # print(req.status_code, 'domain 2')
            # if req.status_code == 200:

                # newArray.append(obj)
            newArray.append(obj)
    return newArray
