from configparser import ConfigParser
config = ConfigParser()
#Read
config.read('configu.ini')
users  = list(config['users'])
users_values = []
key =0
for keyy in users:
    users_values.append(config.get('users', str(keyy)))
for keys in users:
    key += 1
    if not str(keys)=='key'+str(key):
        print("falta "+'key'+str(key))
        break
    else:
        print(str(keys))
a =len(users) - key +1
b = len(users)-a
print(a)
print(b)

for k in range(b,len(users)):
    config.remove_option('users','key'+str(k+2))
    config.set('users','key'+str(k+1),users_values[k])
#sections
#config.add_section('test')
#config.add_section('capacity')
#config.add_section('users')
#config.add_section('passwords')
#config.add_section('urls')
#setValues
#config.set('urls','key1', 'https://drive.google.com/drive/folders/1EG05wKULF5hZ5Wk6QIn8jUAYaXYfR2Qy?usp=sharing')
#config.set('capacity','key1', '155')
#config.remove_option('users', 'key1')
#config.set('users', 'key1', 'julian')
#config.set('passwords', 'key1', '0000')
#config.set('passwords', 'key2', '1111')
#Writing
with open('configu.ini', 'w') as f:
    config.write(f)
#NO BORRAR PORFA