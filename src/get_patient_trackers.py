import json

from box_sdk_gen import BoxClient, BoxDeveloperTokenAuth

def authenticate_box():
    """Authenticate with Box API"""

    # Open config json where developer key is stored
    # Developer key can be generated at
    # https://app.box.com/developers/console
    with open("config.json", "r" ) as f:
        config = json.load(f)

    # Authenticate using the dev token
    BoxDeveloperTokenAuth = BoxDeveloperTokenAuth(token=config["developer_token"])

    return BoxClient(auth=BoxDeveloperTokenAuth)



#for item in BoxClient.folders.get_folder_items('0').entries:
#    print(item.name)
