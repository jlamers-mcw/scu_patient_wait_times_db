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

def find_folder_by_path(client, path_components):
    """Navigate through folder hierarchy to find target folder"""
    current_folder = client.folder('0') # Start at root

    for folder_name in path_components:
        items = current_folder.get_items()
        found = False

        for item in items:
            if item.type == 'folder' and item.name == folder_name:
                current_folder = client.folder(item.id)
                found = True
                print(f"Found folder: {folder_name}")
                break

        if not found:
            raise ValueError(f"Folder '{folder_name}' not found in path")

