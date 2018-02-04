import json
import requests

def sendResquest(url):
	return requests.get(url)

classMap = {0: "None",
            1: "Warrior",
            2: "Paladin",
            3: "Hunter",
            4: "Rogue",
            5: "Priest",
            6: "Death Knigth",
            7: "Shaman",
            8: "Mage",
            9: "Warlock",
            10: "Monk",
            11: "Druid",
            12: "Demon Hunter"
            }

base = "https://eu.api.battle.net/wow/character/"
end = "?fields=items&locale=en_GB&apikey=54ynts6k49dsq5vqm85ecmask7gmjkqa"

guildURI = "https://eu.api.battle.net/wow/guild/%20Aggra%20(Português)/For%20The%20Invicta?fields=members&locale=en_GB&apikey=54ynts6k49dsq5vqm85ecmask7gmjkqa"
Resp = sendResquest(guildURI)
j = json.loads(Resp.content)

n = 0
for i in j["members"]:
	member = i.get("character")
	level = member.get("level")
	pClass = classMap.get(member.get("class"))
	name = member.get("name")
	realm = member.get("realm").replace(" ", "%20")

	if level>=110 and pClass=="Hunter" or pClass=="Priest" or pClass=="Rogue":
		res = sendResquest(base + realm + "/" + name + end)
		p = json.loads(res.content)

		if p is not None:
			items = p.get("items")

			if items is not None:
				ilvl = items.get("averageItemLevelEquipped")

				if ilvl is not None:
					if ilvl>=915 and ilvl<930:
						n = n + 1
						print("\tName:{}".format(name))
						print("\tClass:{}".format(pClass))
						print("\tLevel:{}".format(level))
						print("\tItem Level:{}".format(ilvl))
						print("")




print("Number of Players:{}".format(n))