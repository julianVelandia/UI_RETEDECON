from configparser import ConfigParser
config = ConfigParser()

config.read('config.ini')
config.add_section('capacity')
config.set('capacity','set1', '155')

config.add_section('users')
config.set('users', 'key1', 'SebastianCubides')
config.set('users', 'key2', 'JulianVelandia')

config.add_section('passwords')
config.set('passwords', 'key1', '0000')
config.set('passwords', 'key2', '1111')

with open('config.ini', 'w') as f:
    config.write(f)

#NO BORRAR PORFA