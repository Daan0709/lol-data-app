import json

def load_champions_file():
    with open('champions.json', encoding="utf8") as file:
        data = json.load(file)

    return data

def get_all_champs():
    return load_champions_file()

def get_champ_by_name(name):
    champions = load_champions_file()
    name = name.replace(" ", "").lower()
    for champion in champions:
        if champion['name'].replace(" ", "").lower() == name:
            return champion


def get_champ_by_id(id):
    champions = load_champions_file()
    for champion in champions:
        if champion['id'] == id:
            return champion

def get_champs_by_trait(trait, value):
    champions = load_champions_file()
    list_of_champions = []

    for champion in champions:
        champ_value = champion['stats'][trait]
        if int(champ_value) == int(value):
            list_of_champions.append(champion)

    return list_of_champions


def get_champs_containing(str):
    champions = load_champions_file()
    list_of_champions = []
    str = str.lower()
    for champion in champions:
        if str in champion['name'].lower():
            list_of_champions.append(champion)
    return list_of_champions


# print(get_champs_containing("nn"))
# print(get_all_champs())
# print(get_champ_by_name("aurelion Sol"))
# print(get_champs_by_trait('movespeed', '325'))