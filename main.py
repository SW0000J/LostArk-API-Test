#############################################
# Title: LostArk API Test Code
# Create Date: 2022-12-08
# Update Data: 2022-12-08
# License: MIT LICENSE
# Description: Just Test API with Python Code
#############################################


import json
import requests as r
# import urllib.request as urlr
# import urllib.parse as urlp

LOA_API = "INPUT YOUR API"
LOA_URL = "https://developer-lostark.game.onstove.com"


headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + LOA_API
}


def GetStirng(string : str) -> str:
    return input(f"Input {string}'s Name > ")


def MainMenu() -> int:
    print("****** LOA API USE ******")
    print("1. Get News API ! ! ! ! !")
    print("2. Get Characters API ! !")
    print("3. Get Armories API ! ! !")
    print("4. Get Guilds API ! ! ! !")
    print("5. Get Auctions API ! ! !")
    print("6. Get Markets API. ! ! !")

    print("\n0. Close LOA API. ! ! ! !")

    return int(input("Input API's Number >>>>> "))


def ArmoriesMenu() -> int:
    print("\n**** LOA AMORIES USE ****")
    print("1. Get Profiles ! ! ! ! !")
    print("2. Get Equipments ! ! ! !")
    print("3. Get Avatars. ! ! ! ! !")
    print("4. Get Combat-Skills. ! !")
    print("5. Get Engravings ! ! ! !")
    print("6. Get Cards. ! ! ! ! ! !")
    print("7. Get Gems ! ! ! ! ! ! !")
    print("8. Get Colosseums ! ! ! !")
    print("9. Get Collectibles ! ! !")

    print("\n0. Back to Select ! ! ! !")

    return int(input("Input Armories Number >>>>> "))


def AuctionsMenu() -> int:
    print("\n*** LOA AUCTIONS USE. ***")
    print("1. Get Options. ! ! ! ! !")
    print("2. Get Items. ! ! ! ! ! !")

    print("\n0. Back to Select ! ! ! !")

    return int(input("Input Auctions Number >>>>> "))


def MarketsMenu() -> int:
    print("\n**** LOA AMORIES USE ****")
    print("1. Get Options. ! ! ! ! !")
    print("2. Get Items ID ! ! ! ! !")
    print("3. Get Items. ! ! ! ! ! !")

    print("\n0. Back to Select ! ! ! !")

    return int(input("Input Markets Number >>>>> "))


while True:
    main_num = MainMenu()

    # News API
    if (main_num == 1):
        response = r.get(LOA_URL+"/news/events", headers=headers)
        print(response.json())

    # Characters API
    elif (main_num == 2):
        input_nickname = GetStirng("Character")
        response = r.get(LOA_URL+f"/characters/{input_nickname}/siblings", headers=headers)
        print(response.json())

    # Armories API
    elif (main_num == 3):
        armories_num = ArmoriesMenu()
        input_nickname = GetStirng("Character")

        # Armories - Profiles
        if (armories_num == 1):
            response = r.get(LOA_URL+f"/armories/characters/{input_nickname}/profiles", headers=headers)
            print(response.json())

        # Armories - Equipment
        elif (armories_num == 2):
            response = r.get(LOA_URL+f"/armories/characters/{input_nickname}/equipment", headers=headers)
            print(response.json())

        # Armories - Avatars
        elif (armories_num == 3):
            response = r.get(LOA_URL+f"/armories/characters/{input_nickname}/avatars", headers=headers)
            print(response.json())
        
        # Armories - Combat-Skills
        elif (armories_num == 4):
            response = r.get(LOA_URL+f"/armories/characters/{input_nickname}/combat-skills", headers=headers)
            print(response.json())

        # Armories - Engravings
        elif (armories_num == 5):
            response = r.get(LOA_URL+f"/armories/characters/{input_nickname}/engravings", headers=headers)
            print(response.json())

        # Armories - Cards
        elif (armories_num == 6):
            response = r.get(LOA_URL+f"/armories/characters/{input_nickname}/cards", headers=headers)
            print(response.json())

        # Armories - Gems
        elif (armories_num == 7):
            response = r.get(LOA_URL+f"/armories/characters/{input_nickname}/gems", headers=headers)
            print(response.json())

        # Armories - Colosseums
        elif (armories_num == 8):
            response = r.get(LOA_URL+f"/armories/characters/{input_nickname}/colosseums", headers=headers)
            print(response.json())

        # Armories - Collectibles
        elif (armories_num == 9):
            response = r.get(LOA_URL+f"/armories/characters/{input_nickname}/collectibles", headers=headers)
            print(response.json())

        # Armories - Exit Armories
        elif (armories_num == 0):
            pass

    # Guilds
    elif (main_num == 4):
        input_server = GetStirng("Server")
        response = r.get(LOA_URL+f"/guilds/rankings?serverName={input_server}", headers=headers)
        print(response.json())
    
    # Auctions
    elif (main_num == 5):
        auctions_num = AuctionsMenu()

        # Auctions - Get Options
        if (auctions_num == 1):
            response = r.get(LOA_URL+"/auctions/options", headers=headers)
            print(response.json())

        # Auctions - Search items
        elif (auctions_num == 2):
            
            # Have to edit to search what you want
            data = {
                "ItemLevelMin": 0,
                "ItemLevelMax": 0,
                "ItemGradeQuality": 0,
                "SkillOptions": [
                    {
                    "FirstOption": 0,
                    "SecondOption": 0,
                    "MinValue": 0,
                    "MaxValue": 0
                    }
                ],
                "EtcOptions": [
                    {
                    "FirstOption": 0,
                    "SecondOption": 0,
                    "MinValue": 0,
                    "MaxValue": 0
                    }
                ],
                "Sort": "BIDSTART_PRICE",
                "CategoryCode": 0,
                "CharacterClass": "string",
                "ItemTier": 0,
                "ItemGrade": "string",
                "ItemName": "string",
                "PageNo": 0,
                "SortCondition": "ASC"
            }
            data = json.dumps(data)

            response = r.post(LOA_URL+"/auctions/items", headers=headers, data=data)
            print(response.json())

        # Auctions - Exit Armories
        elif (auctions_num == 0):
            pass

    # Markets
    elif (main_num == 6):
        markets_num = MarketsMenu()

        # Markets - Get Options
        if (markets_num == 1):
            response = r.get(LOA_URL+"/markets/options", headers=headers)
            print(response.json())

        # Markets - Get items id
        if (markets_num == 2):
            item_id = int(input("Input Market ID >>>>> "))
            response = r.get(LOA_URL+f"/markets/items/{item_id}", headers=headers)
            print(response.json())

        # Markets - Search items
        if (markets_num == 3):

            # Have to edit to search what you want
            data = {
                "Sort": "GRADE",
                "CategoryCode": 0,
                "CharacterClass": "string",
                "ItemTier": 0,
                "ItemGrade": "string",
                "ItemName": "string",
                "PageNo": 0,
                "SortCondition": "ASC"
            }
            data = json.dumps(data)

            response = r.post(LOA_URL+"/auctions/items", headers=headers, data=data)
            print(response.json())

        # Markets - Exit Armories
        elif (markets_num == 0):
            pass

    # Exit API's Menu
    elif (main_num == 0):
        break