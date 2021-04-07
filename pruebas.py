from configparser import ConfigParser
config = ConfigParser()
#Read
config.read('config.ini')
#sections
#config.add_section('capacity')
#config.add_section('users')
#config.add_section('passwords')
#config.add_section('urls')
#setValues
config.set('urls','key1', 'https://drive.google.com/drive/folders/1EG05wKULF5hZ5Wk6QIn8jUAYaXYfR2Qy?usp=sharing')
#config.set('capacity','key1', '155')
#config.set('users', 'key1', 'SebastianCubides')
#config.set('users', 'key2', 'JulianVelandia')
#config.set('passwords', 'key1', '0000')
#config.set('passwords', 'key2', '1111')
#Writing
with open('config.ini', 'w') as f:
    config.write(f)
#NO BORRAR PORFA