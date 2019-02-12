import requests
import json
import sys

baseUrl = "https://query.wikidata.org/sparql?format=json&query="

games = json.loads(open('./parsedGame.json','r').read())

uriGame = []
i = 0
length = len(games)

for game in games:
    name = game['name']
    query = "SELECT ?game WHERE { ?game wdt:P31 wd:Q7889. \
        ?game rdfs:label ?itemLabel. \
        FILTER(CONTAINS(LCASE(?itemLabel), LCASE(\""+ name +"\"))). \
        } limit 1"
    try:
        req = requests.get(baseUrl+query).text
        jsonReq = json.loads(req)

        if not len(jsonReq['results']['bindings']) == 0 :
            game["uri"] = jsonReq['results']['bindings'][0]["game"]["value"]
            print(game['uri'])
    except:
        print("QUERY FAILED")
        print(query)

    i+=1
    print(str(i) + " / " + str(length))

file = open('uriGame.json','w')

file.write(json.dumps(games))

