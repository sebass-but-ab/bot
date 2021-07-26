
import json

async def addDataU(uid):
  
  user = await getDataU()
  if str(uid) in user:
    return False
  else:
    user[str(uid)] = {}
    user[str(uid)]["color"] = 'ffff00'
    user[str(uid)]["familyFriendly"] = 0
    user[str(uid)]["sniped"] = 1
    user[str(uid)]["dmblocker"] = 0

  with open("./json/userSettings.json","w") as f:
    json.dump(user,f)
  return True

async def getDataU():
  with open("./json/userSettings.json","r") as f:
    users = json.load(f)
  return users

async def addData(guildId):
  
  guilds = await getData()
  if str(guildId) in guilds:
    return False
  else:
    
    guilds[str(guildId)] = {}
    guilds[str(guildId)]["Nword"] = 0
    guilds[str(guildId)]["Fword"] = 0
    guilds[str(guildId)]["Cword"] = 0
    guilds[str(guildId)]["Prefix"] = '$'
    
    

  with open("./json/serverData.json","w") as f:
    json.dump(guilds,f)
  return True

async def getData():
  with open("./json/serverData.json","r") as f:
    guilds = json.load(f)
  return guilds

async def colorSetup(uid):
  
  await addDataU(uid)
  users = await getDataU()
  color = users[str(uid)]["color"]
  return color


async def changeff(string):
  string = string.replace("fuck", "f**k")
  string = string.replace("bitch", "bi**h")
  string = string.replace("shit", "sh*t")
  string = string.replace("ass", "a**")
  string = string.replace("bastard", "b*stard")
  string = string.replace("dick", "d**k")
  string = string.replace("penis","pp")
  string = string.replace("vagina","vag*na")
  return string
  


async def familyFriendlySetup(uid):
  await addDataU(uid)
  users = await getDataU()
  state = users[str(uid)]["familyFriendly"]
  
  if state == 1:
    return True
  if state == 0:
    return False




async def addDataSnipe(uid):
  
  user = await getDataSnipe()
  if str(uid) in user:
    return False
  else:
    user[str(uid)] = {}
    user[str(uid)]["deletedMessage"] = ''
    user[str(uid)]["date"] = ''
    


  with open("./json/userSnipeCache.json","w") as f:
    json.dump(user,f)
  return True

async def getDataSnipe():
  with open("./json/userSnipeCache.json","r") as f:
    users = json.load(f)
  return users


