import json

#format the file genre into usable array

games = json.loads(open('./details.json','r').read())

gameOutput = []

for game in games:
    genreStr = game['genre']
    genres = genreStr.split(',')

    genreArray = []

    for genre in genres:
        genreArray.append(genre.replace(' ',''))

    game['genre'] = genreArray
    print(game['genre'])

file = open('parsedGame.json','w')

file.write(json.dumps(games))