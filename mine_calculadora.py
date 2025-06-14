#Função para somar dois números 
def soma(n1,n2):
    resultado = n1 + n2
    print(f"O resultado da soma é: {resultado}")

#Função para subtrair dois números     
def subtracao(n1,n2):
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado}")

#Função para multiplicar dois números 
def multiplicacao(n1,n2):
    resultado = n1 * n2
    print(f"O resultado da Multiplicação é: {resultado}")

#Função para dividir dois números 
def divisao(n1,n2):
    resultado = n1 / n2
    print(f"O resultado da Divisão é: {resultado}")    

#Apresentação
nome = input('Seja bem-vindo à sua calculadora em Python. Para começarmos, gostaria de saber primeiro o seu nome: ')

print(f"Seja bem-vindo, {nome}!")

#Começando o looping do programa
while True:
  try:
    n1 =float(input("Por gentileza, diga o primeiro número da sua preferência: "))
    print(f"Certo, o número digitado foi: {n1}")
  except ValueError:
    print("Esse número não é válido")
    continue
  try:  
    n2 = float(input("Agora digite o Segundo Número: "))
    print(f"Certo, o segundo número digitado foi: {n2}")
  except ValueError:
    print("Esse número não é válido")
    continue
    
  
  operador = input("Agora gostaria que você me falasse o operador desejado:\n[So]ma \n[Su]btração \n[M]ultiplicação \n[D]ivisão \n").lower()

  #Caso o cliente escolha soma...

  if operador == "so":
    soma(n1,n2)
    outro = input("Gostaria de falar outro número [S]im ou [N]ão?: ").lower()
    if outro == "s":
      continue
    if outro == "n":
      print("Então até logo, e volte quando precisar!")
      break
    else: 
      print("Não consegui entender, com isso iremos finalizar por aqui, muito obrigado!!")
      break
  
  #Caso o cliente escolha subtração
  
  if operador == "su":
    subtracao(n1,n2)
    outro =  input("Gostaria de falar outro número [S]im ou [N]ão?: ").lower()
    if outro == "s":
      continue
    if outro == "n":
      print("Então até logo, e volte quando precisar!")
      break
    else: 
      print("Não consegui entender, com isso iremos finalizar por aqui, muito obrigado!!")
      break

  #Caso o cliente escolha multiplicação
  
  if operador == "m":
    multiplicacao(n1,n2)
    outro =  input("Gostaria de falar outro número [S]im ou [N]ão?: ").lower()
    if outro == "s":
      continue
    if outro == "n":
      print("Então até logo, e volte quando precisar!")
      break
    else: 
      print("Não consegui entender, com isso iremos finalizar por aqui, muito obrigado!!")
      break

  #Caso o cliente escolha divisão
  
  if operador == "d":
    divisao(n1,n2)
    outro =  input("Gostaria de falar outro número [S]im ou [N]ão?: ").lower()
    if outro == "s":
      continue
    if outro == "n":
      print("Então até logo, e volte quando precisar!")
      break
    else: 
      print("Não consegui entender, com isso iremos finalizar por aqui, muito obrigado!!")
      break
  else:
    print("Não identificamos o operador, tente novamente...")
    continue