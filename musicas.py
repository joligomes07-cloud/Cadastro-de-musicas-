from arquivos import (
    ler_ultimo_codigo,
    atualizar_ultimo_codigo,
    salvar_musica,
    ler_musicas,
    sobrescrever_musicas
)


def cadastrar_musica():
    titulo = input("Título da música: ")
    artista = input("Artista: ")
    album = input("Álbum: ")
    duracao = input("Duração (ex: 3:45): ")

    ultimo_cod = ler_ultimo_codigo()
    novo_cod = ultimo_cod + 1

    linha = f"{novo_cod};{titulo};{artista};{album};{duracao}"
    salvar_musica(linha)
    atualizar_ultimo_codigo(novo_cod)

    print("🎶 Música cadastrada com sucesso!")


def listar_musicas():
    musicas = ler_musicas()

    if not musicas:
        print("Nenhuma música cadastrada.")
        return

    for linha in musicas:
        cod, titulo, artista, album, duracao = linha.strip().split(";")
        print(f"""
Código: {cod}
Título: {titulo}
Artista: {artista}
Álbum: {album}
Duração: {duracao}
-------------------------
""")


def deletar_musica():
    cod_excluir = input("Informe o código da música a excluir: ")
    musicas = ler_musicas()
    novas_musicas = []
    encontrado = False

    for linha in musicas:
        cod = linha.split(";")[0]
        if cod == cod_excluir:
            encontrado = True
        else:
            novas_musicas.append(linha)

    if encontrado:
        sobrescrever_musicas(novas_musicas)
        print("Música removida com sucesso!")
    else:
        print("Código não encontrado.")