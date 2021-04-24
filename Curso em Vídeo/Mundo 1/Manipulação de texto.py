f = ('Tenho que fazer um texto grande para que consiga testar coisas interessantes.')

# Fatiamento
print(f)
print(f[4])
print(f[0:4])
print(f[0:20:2])
print(f[0:20:3])
print(f[:5])
print(f[6:])
print(f[3::3])

# Análise
print(len(f))
print(f.count('a'))

# Análise com Fatiamento
print(f.count('a',5,29))
print(f.find('testar'))
print(f.find('Dragão'))
print('Tenho' in f)
print('Lagarto' in f)

# Transformação
print(f.replace('Tenho','Titã'))
print(f.upper())
print(f.lower())
print(f.capitalize())
print(f.title())
print(f.strip())
print(f.rstrip())
print(f.lstrip())

# Divisão
print(f.split())

# Junção
print('-'.join(f))