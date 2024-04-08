import textwrap

def depositar(saldo, operacoes):
  deposito = float(input("Insira o valor deseja depositar: "))
  if float(deposito) <= 0:
    print("O valor a ser depositado precisa ser positivo.")
  else:
    saldo += deposito 
    operacoes.append(f"Deposito: R$ {deposito:.2f}")
    return saldo

def sacar(saldo, numero_saques, LIMITE_SAQUES):
  saque = float(input("Insira o valor deseja sacar: "))
  if float(saque) <= 0:
    print("\nO valor a ser sacado precisa ser maior que zero")
    return saldo, numero_saques
  elif float(saque) > saldo:
    print("\nSaldo insuficiente")
    return saldo, numero_saques
  elif float(saque) > limite:
    print("\nO valor maximo de saque e R$ 500")
    return saldo, numero_saques
  else:
    numero_saques += 1
    if numero_saques > LIMITE_SAQUES:
      print("\nNao foi possivel realizar essa operacao. Limite de saques diarios atingidos!")
      return saldo, numero_saques
    else: 
      saldo -= saque
      print(f"\nsaque no valor de {saque:.2f} realizado com sucesso")
      operacoes.append(f"Saque: R$ {saque:.2f}")
      return saldo, numero_saques

def extrato(saldo):
  if operacoes == []:
    print("\n========== EXTRATO ==========\n")
    print("Nao houveram movimentacoes\n")
    print("Saldo: R$ 0.00 \n")
    print("=============================")
  else:
    print("\n========== EXTRATO ==========\n")
    for operacao in operacoes:
      print(operacao)
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print("=============================")

def verificar_cpf(cpf):
  for usuario in usuarios:
    if cpf == usuario['cpf']:
      return True
  return False

def criar_usuario():
  nome = input("Informe seu nome: ")
  data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
  while True:
    cpf = input("Informe seu CPF: ")
    if verificar_cpf(cpf):
      print("CPF já cadastrado. Por favor, insira outro CPF.")
    else:
      break
  rua = input("informe nome da Rua e numero: ")
  bairro = input("Informe o bairro: ")
  cidade = input("Informe a cidade: ")
  estado = input("Informe iniciais do estado: ")
  endereco = (f"{rua} - {bairro} - {cidade}/{estado}")
  usuario = {
    'nome': nome,
    'data_nascimento': data_nascimento,
    'cpf': cpf,
    'endereco': endereco
  }
  usuarios.append(usuario)
  print("\nUsuario criado com sucesso!\n")
  print(f"Dados do usuario: \n{nome}\n{data_nascimento}\n{cpf}\n{endereco}")

def criar_conta(usuario, agencia, numero_conta):
  cpf = input("Informe o CPF do usuario: ")

  for usuario in usuarios:
    if usuario['cpf'] == cpf:
      print("\nConta criada com sucesso!")
      conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
      print(conta)
      return conta

  print ("\nUsuario nao encontado! Operacao encerrada!")

def listar_contas(contas):
  for conta in contas:
    linha = f"""\
      agencia: \t{conta['agencia']}
      C/C: \t\t{conta['numero_conta']}
      Titular:\t{conta['usuario']['nome']}
    """
    print("=" * 100)
    print(textwrap.dedent(linha))

def listar_usuarios(usuarios):
  for usuario in usuarios:
    print(usuario)

menu = """
[c] Criar Usuario
[lu] Listar usuarios
[nc] Criar Conta
[lc] Listar Contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

operacoes = []
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
numero_conta = 1
AGENCIA = "0001"
contas = []

while True:
  opcao = input(menu)

  if opcao == "c":
    usuario = criar_usuario()
  
  elif opcao == "lu":
    listar_usuarios(usuarios)

  elif opcao == "nc":
    conta = criar_conta(usuarios, AGENCIA, numero_conta)

    if conta:
      contas.append(conta)
      numero_conta += 1

  elif opcao == "lc":
    listar_contas(contas)

  elif opcao == "d":
    saldo = depositar(saldo, operacoes)
    extrato(saldo)

  elif opcao == "s":
    saldo, numero_saques = sacar(saldo, numero_saques, LIMITE_SAQUES)
    extrato(saldo)
    
  elif opcao == "e":
    extrato(saldo)
  
  elif opcao == "q":
    break
  
  else:
    print("Operacao invalida, por favor selecione novamente a operacao desejada")