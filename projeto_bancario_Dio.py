from datetime import datetime

saldo = 0
limite= 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

print("Bem-vendo  ao Sistema Bancario DIO!")
print("======================")

while True:
	print("           MENU")
	print("====================")
	print("""
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair""")
	print(f"\nSaques restantes pra hoje: {LIMITE_SAQUES - numero_saques}")
	print("=============================")
	
	opcao = int(input("Escolha uma opção(use apenas Numeros): "))
	
	if opcao == 1:
		valor = float(input("Informe o Valor do Deposito: R$"))
		if valor > 0:
			saldo += valor
			data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
			extrato.append(f"{data} | Deposito: R$ {valor:.2f}")
			print("■DEPOSITO REALIZADO COM SUCESSO")
		else:
			print("Valor invalido para")
	elif opcao == 2:
		valor = float(input("Digite o valor pravo Saque: R$ "))
		if valor > saldo:
			print("\nSALDO INSUFICIENTE!\n")
		elif valor > limite:
			print("\no valor excende  o Limite de R$ 500.00 por saque!\n")
		elif numero_saques >= LIMITE_SAQUES:
			print("\nLimite diario de saque atingido!\n")
		elif valor >0:
			saldo -= valor
			numero_saques += 1
			data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
			extrato.append(f"{data} | Saque:	R$ {valor:.2f}")
			print("SAQUE REALIZADO COM SUCESSO!")
		else:
			print("Valor invalido pra o Saque!")
	elif opcao ==3:
			print("\nEXTRATO==============================")
			if not extrato:
				print("nao foram realizados movimentacoes.")
			else:
				for linha in extrato:
					print(linha)
			print("======================================")
			print(f" Saldo atual R$ {saldo:.2f}")
			print("======================================")
	elif opcao ==4:
		print("OBRIGADO POR USAR O SISTEMA BANCARIO")
		print("SAINDO...")
		break
	else:
		print("Operacao Invalida. Tente Novamente")