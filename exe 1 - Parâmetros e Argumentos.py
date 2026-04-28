#Parâmetros com valor padrão (Default)
def saudacao(nome,mensagem = "Bem-Viado!"):
    print(f"Olá {nome}! {mensagem}")
nome = input("Digite seu nome: ")
saudacao(nome)

#Argumentos nomeados (Keyword args)
def criar_usuario(nome,idade, admin=False):
    print(f"{nome} | {idade} anos |admin={admin}")
nome_usuario = input("Digite seu Usuario: ")
idade_usuario = input("Digite sua idade: ")
criar_usuario(nome_usuario, idade_usuario)