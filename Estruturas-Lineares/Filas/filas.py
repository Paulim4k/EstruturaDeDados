From collections imprt deque
def exemplo_fila()
# Criando uma fila usando deque
fila = daque()

# Adicionando elemntos à fila
fila.append("Tarefa 1")
fila.append("Tarefa 2")
fila.append("Tarefa 3")

# Mostrando a fila 
print("Fila atual:", list(fila))

# processando a fila (removendo a primeiro elemento)
While fila:
print(f"Processando: {fila.popleft()}")
