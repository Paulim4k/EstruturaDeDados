def exemplo_pilha():
  # Criando uma pilha usando uma lista
  pilha = []

#Adicionando elemento à pilha ( empilhando )
pilha.append ("Intem 1")
pilha.append ("Intem 2")
pilha.append ("Intem 3")

# Mostrando a pilha 
print("Pilha atual:", pilha)

# Processando a pilha (removendo o último elemento )
While pilha:
    print(f"removendo: {pilha.pop()}")
