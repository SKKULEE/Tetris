#Built-in Modules *************************************************************

import os



#Functions ********************************************************************

def resource_path(relative_path: str) -> str:
    try:
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def game_folder_path(realative_path: str = "") -> str:
    app_data = os.getenv("APPDATA")
    game_folder_path = os.path.join(app_data, "Tetris_byLCG")
    target_path = os.path.join(game_folder_path, realative_path)
    return target_path

def encode(content: str) -> str:
    temp = "".join(["0001"] + ["%03d"%ord(i) for i in content] + ["1000"])[::-1]
    return "".join(chr(int(temp[i:i+4])) for i in range(0, len(temp), 4))

def decode(content: str) -> str:
    temp = "".join(["%04d"%ord(i) for i in content]).strip('0')[-2:0:-1]
    return "".join([chr(int(temp[i:i+3])) for i in range(0, len(temp), 3)])

def game_file_read() -> str:
    file_path = game_folder_path("data.dat")
    data_file = open(file_path, 'r')
    content = decode(data_file.read())
    data_file.close()
    return content

def game_file_write(content: str) -> None:
    file_path = game_folder_path("data.dat")
    data_file = open(file_path, 'w')
    data_file.write(encoded(content))
    data_file.close()

def game_folder_recover() -> None:
    os.mkdir(game_folder_path())
    new_data_file = open(game_folder_path("data.dat"), 'w')
    
    default_content = """I-mino color: (140, 255, 251)
L-mino color: (255, 127, 039)
J-mino color: (063, 072, 204)
O-mino color: (255, 242, 000)
S-mino color: (147, 255, 014)
T-mino color: (184, 061, 186)
Z-mino color: (236, 028, 036)"""

    new_data_file.write(encoded(default_content))
    new_data_file.close()



#Variables ********************************************************************

font = None #추가 예정