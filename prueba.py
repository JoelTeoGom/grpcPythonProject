import prueba

# Crear una instancia del cliente Redis
redis_client = prueba.Redis(host='localhost', port=6379, db=0)

# Obtener todas las claves
claves = redis_client.keys('*')

# Obtener los valores asociados a las claves
valores = redis_client.mget(claves)

# Imprimir los valores
for valor in valores:
    print(valor)
