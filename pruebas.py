from configparser import ConfigParser
config = ConfigParser()

config.read('config.ini')
config.add_section('capacidad')
config.set('capacidad','set1', '155')

config.add_section('usuarios')
config.set('usuarios', 'key1', 'SebastianCubides')
config.set('usuarios', 'key2', 'JulianVelandia')

config.add_section('contraseñas')
config.set('contraseñas', 'key1', '0000')
config.set('contraseñas', 'key2', '1111')

with open('config.ini', 'w') as f:
    config.write(f)

#NO BORRAR PORFA