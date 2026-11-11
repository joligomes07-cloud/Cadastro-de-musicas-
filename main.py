from arquivos import inicializar_arquivos
from musicas import cadastrar_musica, listar_musicas, deletar_musica
from menu import mostrar_menu


def main():
    print("Sistema de Catálogo de Músicas")
    inicializar_arquivos()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_musica()
        elif opcao == "2":
            listar_musicas()
        elif opcao == "3":
            deletar_musica()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")


main()