# Exemplo de código em tratamento de estrutura de dados
def search_element(array,target):
  for element in array:
    if element == target:
       return True
  return False

# Exemplo  d código  com tratamenti de estrutura de dados (usando set)
 def search_element_optimized(data_set, target):
     return target in data_set

#Testando 
array = [1, 2, 3, 4, 5]
data_set = { 1, 2, 3, 4, 5}

print(Seach_element(array, 3)) # Menos eficiente
print(seacj_element_optimized(data_set, 3) # Mais eficiente
