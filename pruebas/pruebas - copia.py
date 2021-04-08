from configparser import ConfigParser
config = ConfigParser()
#Read
config.read('config.ini')
#Check if Pass is Correct
a=list(config['passwords'])
b=list(config['users'])
correct=0
correct2=0
usuarios = []
for key in a:
    contras = [config.get('passwords', str(key))]
    if '0000' == config.get('passwords',str(key)):
        indC = contras.index('0000')
        correct = 1
        print(indC)
    else:
        correct = 0
for key in b:
    usuarios.append(config.get('users', str(key)))

if 'JulianVelandia' in usuarios :

    print(usuarios.index('JulianVelandia'))
    correct2 = 1
else:
    print('E')
    correct2 = 0
'''
if correct==1 and correct2==1 and indU==indC:
    print(1)
else:
    print(0)
'''
#print (config.get('capacity', 'set1'))# -> "value1"
#print (config.get('users', 'key1')) # -> "value2"
#print (config.get('passwords', 'key2'))# -> "value3"
#a=list(config['passwords'])
#NO BORRAR PORFA