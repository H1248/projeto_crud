def menu_principal():
    print("Menu Principal:")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")

def menu_operacoes():
    print("\nMenu de Operações:")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu principal")

# Função para incluir estudantes na lista
def incluir_estudante(lista_estudantes):
    nome = input("Digite o nome do estudante: ")
    lista_estudantes.append(nome)
    print("Estudante adicionado com sucesso!")

# Função para listar estudantes
def listar_estudantes(lista_estudantes):
    if not lista_estudantes:
        print("Não há estudantes cadastrados.")
    else:
        print("Lista de estudantes cadastrados:")
        for estudante in lista_estudantes:
            print("-", estudante)

# Função principal
def main():
    lista_estudantes = []

    while True:
        print("\nMENU PRINCIPAL")
        print("1. Estudantes")
        print("2. Disciplinas")
        print("3. Professores")
        print("4. Turmas")
        print("5. Matrículas")
        print("6. Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == '1':
            while True:
                print("\nMENU DE OPERAÇÕES DE ESTUDANTES")
                print("1. Incluir")
                print("2. Listar")
                print("3. Atualizar (EM DESENVOLVIMENTO)")
                print("4. Excluir (EM DESENVOLVIMENTO)")
                print("5. Voltar ao menu principal")

                opcao_estudantes = input("Selecione uma opção: ")

                if opcao_estudantes == '1':
                    incluir_estudante(lista_estudantes)
                elif opcao_estudantes == '2':
                    listar_estudantes(lista_estudantes)
                elif opcao_estudantes in ['3', '4']:
                    print("EM DESENVOLVIMENTO")
                elif opcao_estudantes == '5':
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao in ['2', '3', '4', '5']:
            print("EM DESENVOLVIMENTO")
        elif opcao == '6':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
