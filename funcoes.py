import os
from colorama import init, Fore
from pprint import pprint
import csv

init(autoreset=True)

orcamento = []
qnt_vgs_garagem = 0

#Função para limpar tela do terminal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#Função que exibe o menu inicial
def exibir_menu():
    print(f"\n\n{Fore.GREEN}================MENU INICIAL================")
    print(f"{Fore.GREEN}1. Orçamento")
    print(f"{Fore.GREEN}0. Sair do Menu")
    print(f"{Fore.GREEN}============================================")

#Função que exibe o menu de opções para escolha da locação
def exibir_menu_locacao():
    print(f"{Fore.GREEN}================MENU DE LOCAÇÃO================")
    print(f"{Fore.GREEN}1. Casa")
    print(f"{Fore.GREEN}2. Apartamento")
    print(f"{Fore.GREEN}3. Estúdio")
    print(f"{Fore.GREEN}===============================================")

#Função que processa a opção escolhida pelo usuário
def processar_opcao(opcao):
    if opcao == "1":
        orcamento.append({
            "Nome Cliente": "",
            "Tipo Locação": "Casa",
            "Valor Aluguel": 900.00,
            "Caracteristica": "1 quarto e sem garagem"
        })
    elif opcao == "2":
        orcamento.append({
            "Nome Cliente": "",
            "Tipo Locação": "Apartamento",
            "Valor Aluguel": 700.00,
            "Caracteristica": "1 quarto e sem garagem"
        })
    elif opcao == "3":
        orcamento.append({
            "Nome Cliente": "",
            "Tipo Locação": "Estúdio",
            "Valor Aluguel": 1200.00,
            "Caracteristica": "1 quarto e sem garagem"
        })
    else:
        print("Opção inválida! Digite uma opção válida!\n")
        exibir_menu_locacao()

#Função coletar dados do cliente
def coletar_informacao():
    nome_cliente = input(f"{Fore.GREEN}Qual o nome do cliente? \n")
    for nome in orcamento:
        nome["Nome Cliente"] = nome_cliente


#Função que exibe as opções de upgrade
def exibir_menu_upgrade(opcao):
    if opcao == "1":
        print(f"{Fore.GREEN}================MENU DE UPGRADE================")
        print(f"{Fore.GREEN}1. Quero casa com 2 quartos")
        print(f"{Fore.GREEN}2. Quero casa com garagem")
        print(f"{Fore.GREEN}3. Quero casa com 2 quartos e com garagem")
        print(f"{Fore.GREEN}4. Não quero upgrade")
        print(f"{Fore.GREEN}===============================================")
    elif opcao == "2":
        print(f"{Fore.GREEN}================MENU DE UPGRADE================")
        print(f"{Fore.GREEN}1. Quero apartamento com 2 quartos")
        print(f"{Fore.GREEN}2. Quero apartamento com garagem")
        print(f"{Fore.GREEN}3. Quero apartamento com 2 quartos e com garagem")
        print(f"{Fore.GREEN}4. Não quero upgrade")
        print(f"{Fore.GREEN}===============================================")
    elif opcao == "3":
        print(f"{Fore.GREEN}================MENU DE UPGRADE================\n")
        print(f"{Fore.BLUE }========TABELA DE PREÇOS (VAGAS GARAGEM)=======")
        print(f"{Fore.BLUE }Até 2 vagas............................R$250,00")
        print(f"{Fore.BLUE }Vagas adicionais...................R$60,00 cada")
        print(f"{Fore.BLUE}===============================================\n\n")
        print(f"{Fore.GREEN}===============================================")

#Função que processa a opção de upgrade escolhida pelo usuário
def processar_opcao_upgrade(opcao, opcao_upgrade, garagem):
    for upgrade in orcamento:    
        if opcao == "1":
            if opcao_upgrade == "1":
                if upgrade["Tipo Locação"] == "Casa":
                    upgrade["Valor Aluguel"] += 250.00
                    upgrade["Caracteristica"] = "2 quartos e sem garagem"
            elif opcao_upgrade == "2":
                if upgrade["Tipo Locação"] == "Casa":
                    upgrade["Valor Aluguel"] += 300.00
                    upgrade["Caracteristica"] = "1 quarto e com garagem"
            elif opcao_upgrade == "3":
                if upgrade["Tipo Locação"] == "Casa":
                    upgrade["Valor Aluguel"] += 550.00
                    upgrade["Caracteristica"] = "2 quartos e com garagem"
            elif opcao_upgrade == "4":
                if upgrade["Tipo Locação"] == "Casa":
                    upgrade["Valor Aluguel"] += 0.00
            else:
                print("Opção inválida! Digite uma opção válida!\n")
                exibir_menu_upgrade()
        elif opcao == "2":
            if opcao_upgrade == "1":
                if upgrade["Tipo Locação"] == "Apartamento":
                    upgrade["Valor Aluguel"] += 200.00
                    upgrade["Caracteristica"] = "2 quartos e sem garagem"
            elif opcao_upgrade == "2":
                if upgrade["Tipo Locação"] == "Apartamento":
                    upgrade["Valor Aluguel"] += 300.00
                    upgrade["Caracteristica"] = "1 quartos e com garagem"
            elif opcao_upgrade == "3":
                if upgrade["Tipo Locação"] == "Apartamento":
                    upgrade["Valor Aluguel"] += 500.00
                    upgrade["Caracteristica"] = "2 quartos e com garagem"
            elif opcao_upgrade == "4":
                    if upgrade["Tipo Locação"] == "Apartamento":
                        upgrade["Valor Aluguel"] += 0.00
            else:
                    print("Opção inválida! Digite uma opção válida!\n")
                    exibir_menu_upgrade()
        elif opcao == "3":
            if garagem == 0:
                if upgrade["Tipo Locação"] == "Estúdio":
                        upgrade["Valor Aluguel"] += 0.00
            elif garagem <= 2:
                if upgrade["Tipo Locação"] == "Estúdio":
                        garagem = str(garagem)
                        upgrade["Valor Aluguel"] += 250.00
                        upgrade["Caracteristica"] = "1 quarto e " + garagem + " vagas de garagem"
            elif garagem > 2:
                valor_garagem = (garagem - 2) * 60.00
                if upgrade["Tipo Locação"] == "Estúdio":
                        upgrade["Valor Aluguel"] += (250.00 + valor_garagem)
                        garagem = str(garagem)
                        upgrade["Caracteristica"] = "1 quarto e " + garagem + " vagas de garagem"
            else:
                print("Opção inválida! Digite uma opção válida!\n")
                exibir_menu_upgrade()
        

#Função que calcula o valor da parcela do contrato
def calcular_parcelamento_contrato():
    for vlr_contrato in orcamento:

        valor_total = 2000.00
        print(f"{Fore.GREEN}O valor para o contrato é de R$ {valor_total:.2f}.")

        try:
            n_parcela = int(input("Você pode parcelar em até 5x sem juros. Em quantas vezes deseja? "))

            if n_parcela < 1 or n_parcela > 5:
                print("Número de parcelas inválido. Escolha entre 1 e 5.")
                return None

            valor_parcela = valor_total / n_parcela
            print(f"Serão {n_parcela} parcelas de R$ {valor_parcela:.2f}\n\n")
            
            vlr_contrato["Valor Contrato"] = valor_total
            vlr_contrato["Quantidade Parcelas"] = n_parcela
            vlr_contrato["Valor Contrato Parcelado"] = round(valor_parcela, 2)

            return valor_parcela

        except ValueError:
            print("Por favor, digite um número válido.")
            return None
        
        

#Função que calcula o desconto caso o tipo locação seja apartamento e o cliente não possua filhos
def calculo_desconto(opcao, filhos):
    for desconto in orcamento:
        if opcao == "2" and filhos == "N":
            desconto["Valor Aluguel"] *= 0.95
        else:
            pass


#Função que calcula as parcelas
def calculo_parcelas():
    for vlr_mensal in orcamento:
        parcelas = vlr_mensal["Quantidade Parcelas"]
        aluguel = vlr_mensal["Valor Aluguel"]
        contrato = vlr_mensal["Valor Contrato Parcelado"]
        for i in range(1, 13):
            chave = f"{i}º mês"

            if i <= parcelas:

                vlr_mensal[chave] = aluguel + contrato
            else:
                vlr_mensal[chave] = aluguel
        

#Criar um arquivo .csv
def exportar_csv(orcamento, nome_arquivo="orcamento.csv"):
    campos = orcamento[0].keys()

    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=campos, delimiter=";")

        writer.writeheader()  
        writer.writerows(orcamento) 

    
#Função que executa o programa como um todo
def executar_programa():
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        if opcao == "0":
            print("Saindo do sistema...")
            break

        limpar_tela()

        exibir_menu_locacao()
        opcao = input("Digite a opção desejada: ")
        limpar_tela()

        processar_opcao(opcao)

        coletar_informacao()
        filhos = input(f"{Fore.GREEN}Cliente possui filhos? |Sim - S | Não - N|: \n").upper()
        limpar_tela()

        exibir_menu_upgrade(opcao)
        if opcao != "3":
            opcao_upgrade = input("Digite a opção desejada: ")
            qnt_vgs_garagem = 0
        else:
            qnt_vgs_garagem = int(input(f"{Fore.GREEN}Quantas vagas de garagem você deseja?"))
            opcao_upgrade = 4
        limpar_tela()
        processar_opcao_upgrade(opcao, opcao_upgrade, qnt_vgs_garagem)

        calculo_desconto(opcao, filhos)
        calcular_parcelamento_contrato()

        calculo_parcelas()

        pprint(orcamento, sort_dicts=False)

        arquivo = input("Deseja gerar um arquivo .CSV com o orçamento aqui computado? |Sim - S | Não - N|: \n").upper()
        if arquivo == "S":
            exportar_csv(orcamento)
