from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

#print (config.get('capacity', 'set1'))# -> "value1"
#print (config.get('users', 'key1')) # -> "value2"
#print (config.get('capacity', 'key3'))# -> "value3"

print(list(config['passwords']))

#NO BORRAR PORFA