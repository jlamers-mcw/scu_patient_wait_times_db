import json

from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth

with open("config.json", "r" ) as f:
    config = json.load(f)

BoxDeveloperTokenAuth = BoxDeveloperTokenAuth(token=config["developer_token"])

BoxClient = BoxClient(auth=BoxDeveloperTokenAuth)

for item in BoxClient.folders.get_folder_items('0').entries:
    print(item.name)
