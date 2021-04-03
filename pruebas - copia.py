from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

#print (config.get('capacidad', 'set1'))# -> "value1"
#print (config.get('usuarios', 'key1')) # -> "value2"
#print (config.get('capacidad', 'key3'))# -> "value3"

print(list(config['contraseñas']))

#NO BORRAR PORFA