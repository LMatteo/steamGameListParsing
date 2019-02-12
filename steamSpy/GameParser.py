import requests as req
import json

# parse file containing app id to get detail on each game

REQUEST_PATH = "http://steamspy.com/api.php?request=appdetails&appid="

gameFile = open('./games.json','r')
gameDict = json.loads(gameFile.read())
print(len(gameDict))

games = []
length = len(gameDict)
i = 0
for game in gameDict:
    games.append(json.loads(req.get(REQUEST_PATH + str(game)).text))
    i+=1
    print( str(i) + " / " + str(length))


gamesDetailFile = open('./details.json','w')
gamesDetailFile.write(json.dumps(games))
gamesDetailFile.close()