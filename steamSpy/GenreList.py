import json 

games = json.loads(open('./parsedGame.json','r').read())

tags = []
print(len(games))
for game in games:
    for tag in game["tags"]:
        game["genre"].append(tag)
    del(game["tags"])    

file = open('taggedGame.json','w')

file.write(json.dumps(games))