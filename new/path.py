import os
def get_path():
    dir = str(os.getcwd())
    str_dir = ''
    for let in dir:
        if ord(let) == 92: let = "/"
        str_dir+= let
    print(str_dir)
    return str_dir
GAME_MODE = "new"
path = get_path() + f"/{GAME_MODE}/"