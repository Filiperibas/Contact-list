def adicionar_contatos(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado na agenda.")
    return

def visualizar_contato(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "❤" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        print(f"{indice} {nome_contato} {favorito}")
    return

def editar_contatos(contatos, indice, propriedades):
    if propriedades == 1:
       novo_nome_contato = input("Qual vai ser o novo nome do contato: ")
    elif propriedades == 2:
        novo_numero_contato = int(input("Qual vai ser o novo numero do contato: "))
    elif propriedades == 3: 
        novo_email_contato = input("Qual vai ser o novo email do contato: ")
    else:
        print("Você digitou uma opção invalida")

    indice_corrigido = indice - 1
    
    if propriedades == 1:
        contatos[indice_corrigido]["nome"] = novo_nome_contato
        print(f"Nome {novo_nome_contato} atualizado com sucesso")
    elif propriedades == 2:
        contatos[indice_corrigido]["telefone"] = novo_numero_contato
        print(f"Número {novo_numero_contato} atualizado com sucesso")
    elif propriedades == 3:
        contatos[indice_corrigido]["email"] = novo_email_contato
        print(f"Email {novo_email_contato} atualizado com sucesso")
    return


contatos = []
while True:
    print("\nAgenda pessoal.")
    print("1. Adicionar um contato.")
    print("2. Visualisar contatos.")
    print("3. Editar contatos.")
    print("4. Favoritar e desfavoritar contatos.")
    print("5. Visualizar contatos favoritos.")
    print("6. Apagar um contato.")
    print("7. Sair do programa")

    escolha = int(input("Digite o numero da opção desejada:"))

    if escolha == 1:
        nome_contato = input("\nQue nome deseja salvar nesse contato: ")
        telefone_contato = int(input("Insira o numero de telefone do contato: "))
        email_contato = input("Insira o email do contato: ")
        adicionar_contatos(contatos, nome_contato, telefone_contato, email_contato)
    elif escolha == 2:
        visualizar_contato(contatos)
    elif escolha == 3:
        visualizar_contato(contatos)
        indice = int(input("\nQual o numero do contato que você quer editar: "))
        print("Qual propriedade do contato você quer alterar: ")
        print("\n1. Nome.")
        print("2. Número.")
        print("3. Email.")
        propriedades = int(input())
        editar_contatos(contatos, indice, propriedades)
    elif escolha == 4:
        pass
    elif escolha == 5: 
        pass
    elif escolha == 6:
        pass 
    elif escolha == 7:
        break

