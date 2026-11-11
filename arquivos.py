import os

PASTA_DADOS = "dados"
ARQUIVO_MUSICAS = os.path.join(PASTA_DADOS, "musicas.txt")
ARQUIVO_COD = os.path.join(PASTA_DADOS, "ultimo_cod.txt")


def inicializar_arquivos():
    if not os.path.exists(PASTA_DADOS):
        os.mkdir(PASTA_DADOS)

    if not os.path.exists(ARQUIVO_MUSICAS):
        open(ARQUIVO_MUSICAS, "w").close()

    if not os.path.exists(ARQUIVO_COD):
        with open(ARQUIVO_COD, "w") as f:
            f.write("0")


def ler_ultimo_codigo():
    with open(ARQUIVO_COD, "r") as f:
        return int(f.read())


def atualizar_ultimo_codigo(cod):
    with open(ARQUIVO_COD, "w") as f:
        f.write(str(cod))


def salvar_musica(linha):
    with open(ARQUIVO_MUSICAS, "a") as f:
        f.write(linha + "\n")


def ler_musicas():
    with open(ARQUIVO_MUSICAS, "r") as f:
        return f.readlines()


def sobrescrever_musicas(linhas):
    with open(ARQUIVO_MUSICAS, "w") as f:
        f.writelines(linhas)