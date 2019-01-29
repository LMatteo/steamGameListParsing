import json

file = open('cpu.json','r')
jsonFile = json.loads(file.read())
jsonarr = jsonFile['root']['tr']

'''
name = elem['td'][0]['a'][1]['#text']
price = elem['td'][1]['a']['#text']
mark = elem['td'][2]
'''
content = []

error = 0
for elem in jsonarr:
    try:
        name = elem['td'][0]['a'][1]['#text']
        price = elem['td'][1]['a']['#text']
        mark = int(elem['td'][2])
        cpu = dict()
        cpu['name'] = name
        cpu['price'] = price
        cpu['score'] = mark

        content.append(cpu) 

    except:
        error =error+1
        #print('error : ' + str(error) + '/' + str(len(jsonarr)))

print(content)