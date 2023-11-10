import pandas
import json

get = pandas.read_excel('WEBSITES_DB.xlsx')


json_str = get.to_json(orient='records')
list_var = json.loads(json_str)


def listArr():
    newArray = []
    for i in list_var:

        if i['domain_initial'] != None:
            
            obj = {'name': i['project_name'], 'url': i['domain_initial']}
            newArray.append(obj)
            
        if i['domain 2'] != None:
            obj = {'name': i['project_name'], 'url': i['domain 2']}
            newArray.append(obj)
    return newArray
