def soma(n1,n2):
    resultado = n1 + n2
    print(f"O resultado da soma é: {resultado}:")
    
def subtracao(n1,n2):
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado}:")

def multiplicaçao(n1,n2):
    resultado = n1 * n2
    print(f"O resultado da Multiplicação é: {resultado}:")

def divisao(n1,n2):
    resultado = n1 / n2
    print(f"O resultado da Divisão é: {resultado}:")    

nome = input('Seja bem vindo a sua cauculadora em Python. Para começarmos, gostaria de saber primeiro o seu nome: ')

print(f"Seja bem vindo {nome}!!")
while True:
  n1 =input("Por gentileza, diga o primeiro número da sua preferência: ")

  if not n1.isdigit():
    print("Infelizmente não conseguimos identificar o número, vamos tentar novamente...")
    continue
  else:
    print(f"Certo, o número digitado foi: {n1}")

  n2 = input("Agora digite o Segundo Número: ")

  if not n2.isdigit():
    print("Infelizmente não conseguimos identificar o número, vamos tentar novamente...")
    continue
  else:
    print(f"Certo, o segundo número digitado foi: {n2}")
  
  operador = input("Agora gostaria que você me falasse o operador desejado:\n[So]ma \n[Su]btração \n[M]ultiplicação \n[D]ivisão \n").lower()

  if operador == "so":
    soma(int(n1),int(n2))
    outro = input("Gostaria de falar outro número [S]im ou [N]ão?: ").lower()
    if outro == "s":
      continue
    if outro == "n":
      print("Então até logo, e volte quando precisar!")
      break
    else: 
      print("Não consegui entender, com isso iremos finalizar por aqui, muito obrigado!!")
      break

  if operador == "su":
    subtracao(int(n1),int(n2))
    outro =  input("Gostaria de falar outro número [S]im ou [N]ão?: ").lower()
    if outro == "s":
      continue
    if outro == "n":
      print("Então até logo, e volte quando precisar!")
      break
    else: 
      print("Não consegui entender, com isso iremos finalizar por aqui, muito obrigado!!")
      break

  if operador == "m":
    multiplicaçao(int(n1),int(n2))
    outro =  input("Gostaria de falar outro número [S]im ou [N]ão?: ").lower()
    if outro == "s":
      continue
    if outro == "n":
      print("Então até logo, e volte quando precisar!")
      break
    else: 
      print("Não consegui entender, com isso iremos finalizar por aqui, muito obrigado!!")
      break
  if operador == "d":
    divisao(int(n1),int(n2))
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












