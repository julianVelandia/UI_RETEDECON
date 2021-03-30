import pandas as pd



i=0
'''
Lista=df['HoraIn']
for hora in range(len(Lista)-1,0,-1):
    
    print(df['HoraIn'][hora])
print(df['HoraIn'][0])
'''

df = open ("DB.csv", "a")

persona = 'prueba,234234,34,345,34534,*,34,True'
df.write(persona)
df.close()