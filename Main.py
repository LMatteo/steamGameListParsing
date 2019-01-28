import requests as req
import json

osList = ['pc_requirements','mac_requirements','linux_requirements']

file = open('gameList.json', 'r')
gameListTxt = file.read()
file.close()
gameList = json.loads(json.loads(gameListTxt))['applist']['apps']

requirements = []
i = 230
del gameList[:i]
written = 0
for var in gameList:
    try:
        name = var['name']
        appid = var['appid']

        parsed = False
        txt = req.get("https://store.steampowered.com/api/appdetails?appids=" + str(appid)).text
        game = (json.loads(txt))[str(appid)]
        i = i + 1
        print(str(i) + " / " + str(len(gameList)))
        print(name)
        print(appid)
        if game['success']:
            game = game['data']
        else:
            continue

        content = dict()
        content['name'] = name
        content['appid'] = appid
        for os in osList:
            content[os] = dict()
            if os in game:
                if 'minimum' in game[os]:
                    content[os]['minimum'] = game[os]['minimum']
                    parsed = True
                if 'recommended' in game[os]:
                    content[os]['recommended'] = game[os]['recommended']
                    parsed = True

        if parsed:
            requirements.append(content)

        written = written + 1
        print("written : " + str(written))
        if (written % 100) == 0:
            file = open('req/requirement' + str(i) +'.json', 'w')
            file.write(json.dumps(requirements))
            file.close()
            print('write!!!!')
            requirements = []
    except:
        print("error?")







