global PlayerList

def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(name, damage=0, defensePower=0):
    return {
        "name": name,
        "score": 0,
        "damage": damage,
        "health": 100,
        "defensePower": defensePower,
        "defense": False
    }

def addPlayer(player):
    global PlayerList
    PlayerList.append(player)

def removePlayer(name):
    global PlayerList
    for player in PlayerList:
        if player["name"] == name:
            PlayerList.remove(player)
            print(f'{name} keluar dari permainan')
            return
    print('There is no player with that name!')

def setPlayer(player, key, value):
    if key in player:
        player[key] = value

def attackPlayer(attacker, target):
    if target["defense"]:
        damage = max(0, attacker["damage"] - target["defensePower"])
        setPlayer(target, "defense", False)
        score = 0.8
    else:
        damage = attacker["damage"]
        score = 1
    
    # hit target

    setPlayer(target, "health", max(0, target["health"] - damage))
    # tambah skor attacker
    setPlayer(attacker, "score", attacker["score"] + score)
    
    

def displayMatchResult():
    global PlayerList
    sortPlayers = sorted(PlayerList, key=lambda p: (-p["score"], -p["health"]))
    
    for rank, player in enumerate(sortPlayers, start=1):
        print(f"Rank {rank}: {player['name']} | Score: {player['score']} | Health: {player['health']}")