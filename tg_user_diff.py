from telethon import TelegramClient, sync
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import json
import os

# NOTE: Rename config.example.json to config.json and update the values in it
config_path = os.path.join(os.path.dirname(__file__), "config.json")
try:
    with open(config_path, "r") as jsonfile:
        config = json.load(jsonfile)
except FileNotFoundError:
    print("Config file not found")
    exit(1)


def get_members(group):
    offset = 0
    limit = 500
    all_participants = {}

    while True:
        participants = client(GetParticipantsRequest(
            group, ChannelParticipantsSearch(''), offset, limit, hash=0
        ))
        if not participants.users:
            break
        for user in participants.users:
            all_participants[user.id] = user
        offset += len(participants.users)

    return all_participants


def build_name(user, userid):
    if user is None:
        return "[Unknown user] [" + str(userid) + "]"
    if user.deleted:
        return "[Deleted user] [" + str(userid) + "]"
    name = user.first_name if user.first_name is not None else ""
    if user.last_name is not None:
        name = name + " " + user.last_name
    if user.username is not None:
        name = name + " (@" + user.username + ")"
    name = name + " [" + str(userid) + "]"
    return name


client = TelegramClient('session', config["api_id"], config["api_hash"])
client.start()

main_group = client.get_entity(config['main_group_id'])
sec_group = client.get_entity(config['second_group_id'])

main_members = get_members(main_group)
sec_members = get_members(sec_group)

users_not_in_main = set(sec_members.keys()) - set(main_members.keys())

print("Users not in main:")
for userid in users_not_in_main:
    print("   " + build_name(sec_members[userid], userid))
